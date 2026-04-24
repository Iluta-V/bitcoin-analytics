
# Bitcoin Analytics

Analysis of Bitcoin network usage from 2009 to 2017 using 492,000 blocks from a Bitcoin Core node.

## Project Description

This project analyzes how Bitcoin usage grew from 2009 to 2017 by examining block data. Key metrics include transaction volume, block size, empty block rate, block intervals, and the impact of SegWit and halving events.

## Installation

1. Clone or download this repository.
2. Install the package in editable mode:

```bash
pip install -e .
```

## Usage

1. Place your CSV file at `data/raw/all_blocks.csv`.  
   Required columns: `height`, `hash`, `timestamp`, `size`, `weight`, `tx_count`.

2. Run the analysis:

```bash
python main.py
```

Charts will be saved as PNG files in the current directory.

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

All dependencies are automatically installed with the package.

## Output

The following charts are generated:

- Block size over time (with 1 MB limit line)
- Daily transaction volume
- SegWit effect (before/after block 481,824)
- Empty block rate over years
- Block interval scatter plot

## Changelog

For a detailed version history, see [CHANGELOG.md](CHANGELOG.md).
