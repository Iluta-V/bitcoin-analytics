import pandas as pd
from .validator import validate_block_hash

def load_blocks(file_path):
    df = pd.read_csv(file_path)
    df['hash'].apply(validate_block_hash)
    return df
