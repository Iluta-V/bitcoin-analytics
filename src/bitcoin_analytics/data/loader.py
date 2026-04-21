import pandas as pd
from .validator import validate_block_hash

def load_blocks(file_path):
    print(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    print(f"   - Rows loaded: {len(df)}")
    print(f"   - Columns: {', '.join(df.columns)}")
    print("   - Validating block hashes...")
    df['hash'].apply(validate_block_hash)
    print("   - Validation OK")
    return df
