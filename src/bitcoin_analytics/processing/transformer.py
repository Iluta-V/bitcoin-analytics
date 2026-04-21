def daily_aggregates(df):
    print("Transforming data...")
    daily = df.groupby('date').agg(
        total_tx=('tx_count', 'sum'),
        avg_block_size_mb=('block_size_mb', 'mean'),
        block_count=('height', 'count')
    ).reset_index()
    print(f"   - Daily records: {len(daily)}")
    return daily
