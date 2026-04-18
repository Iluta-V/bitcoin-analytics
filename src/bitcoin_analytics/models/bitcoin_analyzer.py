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

        plot_block_size(self.df)
        plot_transactions(self.df)
        plot_segwit(self.df)
        plot_empty_rate(empty)
        plot_intervals(intervals)
        return self
