import pandas as pd

def empty_block_rate(df):
    print("Computing metrics...")
    df['year'] = df['timestamp'].dt.year
    # Fixed: select column before apply to avoid FutureWarning
    empty = df.groupby('year')['tx_count'].apply(
        lambda x: (x < 5).mean() * 100
    ).reset_index(name='empty_pct')
    print("   - Empty block rate by year... OK")
    return empty

def block_intervals(df):
    df = df.sort_values('timestamp')
    df['prev'] = df['timestamp'].shift(1)
    df['interval_sec'] = (df['timestamp'] - df['prev']).dt.total_seconds()
    print("   - Block intervals... OK")
    return df.dropna(subset=['interval_sec'])[['height', 'interval_sec']]
