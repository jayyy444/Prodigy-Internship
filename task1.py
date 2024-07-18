def encrypt(text, shift):
    # Initialize the result string
    result = ""

    # Traverse each character in the input text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            # Shift the character and wrap around using modulo operation
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Encrypt lowercase characters
        elif char.islower():
            # Shift the character and wrap around using modulo operation
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # Keep non-alphabetic characters unchanged
        else:
            result += char

    return result

def decrypt(text, shift):
    # Decrypt by reversing the shift
    return encrypt(text, -shift)

# Ask the user for the message to be encrypted/decrypted
text = input("Please enter the message you want to encrypt or decrypt: ")

# Ask the user for the shift value
shift = int(input("Please enter the shift value (positive for encryption, negative for decryption): "))

# Encrypt the input text
encrypted_text = encrypt(text, shift)
print(f"\nEncrypted message: {encrypted_text}")

# Decrypt the encrypted text to verify correctness
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted message (to verify): {decrypted_text}")
