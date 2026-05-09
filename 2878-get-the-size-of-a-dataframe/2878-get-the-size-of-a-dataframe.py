import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(players)
    return [len(df), df.shape[1]]