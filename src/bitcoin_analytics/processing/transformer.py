def daily_aggregates(df):
    daily = df.groupby('date').agg(
        total_tx=('tx_count', 'sum'),
        avg_block_size_mb=('block_size_mb', 'mean'),
        block_count=('height', 'count')
    ).reset_index()
    return daily
