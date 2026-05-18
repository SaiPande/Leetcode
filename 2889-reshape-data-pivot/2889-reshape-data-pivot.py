import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(weather)
    return df.pivot_table(
        columns = 'city',
        index = 'month',
        values = 'temperature'
    )