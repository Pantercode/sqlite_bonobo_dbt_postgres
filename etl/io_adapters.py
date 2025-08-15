etl/io_adapters.py
import sqlite3
import pandas as pd
from sqlalchemy import create_engine, text
from typing import Iterator, Tuple
from .config import SQLITE_PATH, PG_URL, PG_SCHEMA_RAW

# Conexões globais simples (bonobo é single-thread por padrão)
_sqlite_conn = None
_pg_engine = None

def get_sqlite_conn():
    global _sqlite_conn
    if _sqlite_conn is None:
        _sqlite_conn = sqlite3.connect(SQLITE_PATH)
    return _sqlite_conn

def get_pg_engine():
    global _pg_engine
    if _pg_engine is None:
        _pg_engine = create_engine(PG_URL, pool_pre_ping=True)
    return _pg_engine

def list_sqlite_tables() -> list:
    conn = get_sqlite_conn()
    rows = pd.read_sql(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;",
        conn
    )
    return rows["name"].tolist()

def iter_dataframe_chunks(table_name: str, chunksize: int = 100_000) -> Iterator[pd.DataFrame]:
    conn = get_sqlite_conn()
    offset = 0
    while True:
        df = pd.read_sql_query(
            f"SELECT * FROM '{table_name}' LIMIT {chunksize} OFFSET {offset}",
            conn
        )
        if df.empty:
            break
        # normaliza nomes de colunas
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
        yield df
        offset += len(df)

def prepare_raw_schema():
    engine = get_pg_engine()
    with engine.begin() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {PG_SCHEMA_RAW};"))
