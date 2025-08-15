import bonobo
import pandas as pd
from sqlalchemy import text
from .io_adapters import (
    list_sqlite_tables,
    iter_dataframe_chunks,
    get_pg_engine,
    prepare_raw_schema,
)
from .config import PG_SCHEMA_RAW

def start():
    """Inicialização antes do grafo executar."""
    prepare_raw_schema()
    yield from list_sqlite_tables()  # emite cada nome de tabela do SQLite

def extract(table_name: str):
    """Extrai em chunks para não estourar memória."""
    for df in iter_dataframe_chunks(table_name):
        yield table_name, df

def transform(table_name: str, df: pd.DataFrame):
    """Transform simples / normalização leve (o resto no dbt/silver)."""
    from .transforms import coerce_types
    df2 = coerce_types(df)
    yield table_name, df2

def load(table_name: str, df: pd.DataFrame):
    """Carrega no Postgres (schema raw), substituindo na primeira passada e depois append."""
    engine = get_pg_engine()
    table_lower = table_name.lower()

    # Marcador de "primeira escrita" por tabela (em memória de processo)
    if not hasattr(load, "_first_write"):
        load._first_write = set()

    if table_lower not in load._first_write:
        if_exists = "replace"
        load._first_write.add(table_lower)
    else:
        if_exists = "append"

    df.to_sql(
        name=table_lower,
        con=engine,
        schema=PG_SCHEMA_RAW,
        if_exists=if_exists,
        index=False,
        method="multi",
        chunksize=10_000
    )

    # Opcional: analisa/otimiza estatísticas
    with engine.begin() as conn:
        conn.execute(text(f"ANALYZE {PG_SCHEMA_RAW}.{table_lower};"))

def get_graph():
    """
    Pipeline:
      start() -> extract -> transform -> load
    """
    graph = bonobo.Graph()
    graph.add_chain(start, extract, transform, load)
    return graph

def get_services():
    return {}
