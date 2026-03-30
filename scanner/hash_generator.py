# hash_generator.py
# Purpose: Generate MD5 and SHA256 hashes for files

import hashlib
import os

def generate_hashes(file_path):
    """Generate MD5 and SHA256 hash for a given file."""
    
    # Check if file exists
    if not os.path.exists(file_path):
        return None, None
    
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()

    # Read file in chunks (handles large files safely)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
            sha256.update(chunk)

    return md5.hexdigest(), sha256.hexdigest()