import re

def validate_block_hash(block_hash):
    if not re.match(r'^[a-fA-F0-9]{64}$', block_hash):
        raise InvalidBlockDataError(f"Bad hash: {block_hash}")
    return True
