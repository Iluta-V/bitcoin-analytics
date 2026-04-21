from ..data.loader import load_blocks
from ..processing.cleaner import clean_blocks
from ..processing.transformer import daily_aggregates
from ..analysis.metrics import empty_block_rate, block_intervals
from ..visualization.plotter import (
    plot_block_size, plot_transactions, plot_segwit,
    plot_empty_rate, plot_intervals
)

class BitcoinAnalyzer:
    def __init__(self, path):
        self.path = path
        self.df = None

    def load(self):
        self.df = load_blocks(self.path)
        return self

    def clean(self):
        self.df = clean_blocks(self.df)
        return self

    def run(self):
        self.load().clean()
        daily = daily_aggregates(self.df)
        empty = empty_block_rate(self.df)
        intervals = block_intervals(self.df)

        # Save charts (optional: add path if you want)
        plot_block_size(self.df, "block_size_over_time.png")
        plot_transactions(self.df, "transaction_volume.png")
        plot_segwit(self.df, save_path="segwit_comparison.png")
        plot_empty_rate(empty, "empty_block_rate.png")
        plot_intervals(intervals, "block_intervals.png")

        # Print summary statistics
        print("\nSummary Statistics:")
        print(f"   - Total blocks: {len(self.df)}")
        print(f"   - Date range: {self.df['timestamp'].min()} to {self.df['timestamp'].max()}")
        print(f"   - Average block size: {self.df['block_size_mb'].mean():.2f} MB")
        if not empty.empty:
            print(f"   - Empty blocks (<5 tx): {empty['empty_pct'].iloc[-1]:.1f}%")
        print("\nAnalysis complete. Charts saved to current directory.")
        return self
