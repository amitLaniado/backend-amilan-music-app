import hashlib

def hash_password(password: str) -> str:
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the password bytes
    sha256.update(password_bytes)
    
    # Get the hexadecimal representation of the hash
    password_hash = sha256.hexdigest()
    
    return password_hash

# Example usage
password = "my_secure_password"
hashed_password = hash_password(password)
print(f"The SHA-256 hash of the password is: {hashed_password}")
