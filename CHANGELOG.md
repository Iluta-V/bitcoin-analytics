# Changelog

## [1.0] - 2025-04-17
- Initial project setup
- Created package structure
- Added basic modules

## [1.1] - 2025-04-18
- Added data loader with block hash validation (regex)
- Added custom exception `InvalidBlockDataError`
- Added data loader, validator, cleaner, transformer modules

## [1.2] - 2025-04-19
- Added metrics and plotting modules
- Implemented data cleaning (timestamp conversion, date extraction, block size in MB)
- Added daily aggregation using Pandas groupby

## [1.3] - 2025-04-20
- Implemented `BitcoinAnalyzer` class
- Integrated all modules into the main class

## [1.4] - 2025-04-21
- Initial release
- Implemented data loading, cleaning, transformation
- Updated print messages for all modules:
  - `loader.py` – prints loading progress, row count, columns, validation status
  - `cleaner.py` – prints cleaning steps
  - `transformer.py` – prints daily aggregation count
  - `metrics.py` – prints metric computation status
  - `plotter.py` – prints chart generation progress with file names
  - `bitcoin_analyzer.py` – prints summary statistics and completion message

## [1.5] - 2025-04-22
- Added metrics: transaction volume, empty block rate, block intervals


## [1.6] - 2025-04-23
- Made visualizations: block size, transaction volume, SegWit effect, empty blocks, intervals
- All 5 visualisations charts completed
- Wrote `README.md`

## [1.7] - 2025-04-24
- Final integration and testing
- Project complete
