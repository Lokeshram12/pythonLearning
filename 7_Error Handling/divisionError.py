def division(a,b):
    try:
        r=a/b
        # print(r)
        return r
    except ZeroDivisionError:
        print("Division by zero is not possible")
        return 0

ans=division(8,4)
print(ans)
ans=division(5,0)
print(ans)


from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Generate a key (this should be done once and securely stored)
    key = generate_key()
    
    # Message to encrypt
    original_message = "This is a secret message."
    
    # Encrypt the message
    encrypted_message = encrypt_message(original_message, key)
    print("Encrypted:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted:", decrypted_message)
import json

# Encrypt a dictionary
def encrypt_dict(dictionary, key):
    json_data = json.dumps(dictionary)
    encrypted_data = encrypt_message(json_data, key)
    return encrypted_data

# Decrypt a dictionary
def decrypt_dict(encrypted_data, key):
    decrypted_data = decrypt_message(encrypted_data, key)
    dictionary = json.loads(decrypted_data)
    return dictionary

# Example usage
if __name__ == "__main__":
    # Example sensitive data (dictionary)
    sensitive_data = {
        "username": "user123",
        "password": "s3cr3tp@ssw0rd",
        "credit_card": "1234-5678-9101-1121"
    }
    
    # Encrypt the dictionary
    encrypted_data = encrypt_dict(sensitive_data, key)
    print("Encrypted dictionary:", encrypted_data)
    
    # Decrypt the dictionary
    decrypted_data = decrypt_dict(encrypted_data, key)
    print("Decrypted dictionary:", decrypted_data)
