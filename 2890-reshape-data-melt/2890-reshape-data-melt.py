import pandas as pd

def meltTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(weather)
    return df.melt(
        id_vars = ['product'],
        var_name = 'quarter',
        value_name = 'sales'
    )