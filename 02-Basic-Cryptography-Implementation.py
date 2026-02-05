import hashlib

# 1. Caesar Cipher (Symmetric Encryption)
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# 2. SHA-256 Hashing (Modern Standard)
def generate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Testing the implementations
message = "Cybersecurity 2026"
print(f"Original: {message}")
print(f"Cezar Encrypted: {caesar_encrypt(message, 4)}")
print(f"SHA-256 Hash: {generate_sha256(message)}")
