import pandas as pd

def clean_blocks(df):
    print("Cleaning data...")
    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df = df.dropna(subset=['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['block_size_mb'] = df['size'] / 1_000_000
    print("   - Converted timestamp to datetime")
    print("   - Added 'date' and 'block_size_mb' columns")
    return df
