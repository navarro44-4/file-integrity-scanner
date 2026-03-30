# File integrity Scanner
# Author: Victor Navarro
# Purpose: Malware Analysis and Forensic

from scanner.hash_generator import generate_hashes

print("File Integrity Scanner Starting")
print("Version 1.0")
print("-" * 40)

# Test it on our own main.py file!
file = "main.py"
md5, sha256 = generate_hashes(file)

print(f"File: {file}")
print(f"MD5: {md5}")
print(f"SHA256: {sha256}")