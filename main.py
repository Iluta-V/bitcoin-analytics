from bitcoin_analytics.models.bitcoin_analyzer import BitcoinAnalyzer

if __name__ == "__main__":
    analyzer = BitcoinAnalyzer("data/raw/all_blocks.csv")
    analyzer.run()
