def empty_block_rate(df):
    df['year'] = df['timestamp'].dt.year
    empty = df.groupby('year').apply(
        lambda g: (g['tx_count'] < 5).mean() * 100
    ).reset_index(name='empty_pct')
    return empty

def block_intervals(df):
    df = df.sort_values('timestamp')
    df['prev'] = df['timestamp'].shift(1)
    df['interval_sec'] = (df['timestamp'] - df['prev']).dt.total_seconds()
    return df.dropna(subset=['interval_sec'])[['height', 'interval_sec']]
