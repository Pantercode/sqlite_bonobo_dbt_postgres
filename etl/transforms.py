import pandas as pd

def coerce_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform genérico: aqui você pode padronizar tipos simples.
    (Mantenho minimalista; ajustes finos vão para a camada silver do dbt.)
    """
    # remover strings vazias -> None
    df = df.applymap(lambda x: None if isinstance(x, str) and x.strip()=="" else x)
    return df
