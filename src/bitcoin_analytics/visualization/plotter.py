import matplotlib.pyplot as plt

def plot_block_size(df, save_path=None):
    print("Generating charts...")
    daily = df.groupby('date')['block_size_mb'].mean().reset_index()
    plt.figure(figsize=(12,6))
    plt.plot(daily['date'], daily['block_size_mb'])
    plt.axhline(y=1.0, color='r', linestyle='--')
    plt.title('Block Size Over Time')
    plt.xlabel('Date')
    plt.ylabel('Size (MB)')
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print("   [1/5] Block size over time →", save_path)
    plt.show()

def plot_transactions(df, save_path=None):
    daily = df.groupby('date')['tx_count'].sum().reset_index()
    plt.figure(figsize=(12,6))
    plt.plot(daily['date'], daily['tx_count'])
    plt.title('Daily Transactions')
    plt.xlabel('Date')
    plt.ylabel('Transactions')
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print("   [2/5] Transaction volume →", save_path)
    plt.show()

def plot_segwit(df, segwit_block=481824, save_path=None):
    before = df[df['height'] < segwit_block]['weight'].mean()
    after = df[df['height'] >= segwit_block]['weight'].mean()
    plt.figure(figsize=(6,6))
    plt.bar(['Before', 'After'], [before, after])
    plt.title('SegWit Effect')
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print("   [3/5] SegWit comparison →", save_path)
    plt.show()

def plot_empty_rate(empty_df, save_path=None):
    plt.figure(figsize=(10,6))
    plt.plot(empty_df['year'], empty_df['empty_pct'], marker='o')
    plt.title('Empty Blocks (%)')
    plt.xlabel('Year')
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print("   [4/5] Empty block rate →", save_path)
    plt.show()

def plot_intervals(intervals_df, save_path=None):
    plt.figure(figsize=(12,6))
    plt.scatter(intervals_df['height'], intervals_df['interval_sec'], s=1, alpha=0.5)
    plt.axhline(y=600, color='r', linestyle='--')
    plt.title('Block Intervals')
    plt.xlabel('Block Height')
    plt.ylabel('Seconds')
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print("   [5/5] Block intervals →", save_path)
    plt.show()
