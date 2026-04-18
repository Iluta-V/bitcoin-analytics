import pandas as pd

def clean_blocks(df):
    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df = df.dropna(subset=['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['block_size_mb'] = df['size'] / 1_000_000
    return df
