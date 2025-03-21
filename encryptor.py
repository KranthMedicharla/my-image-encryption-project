from PIL import Image
from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate a key for encryption and decryption."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the previously generated key."""
    return open("secret.key", "rb").read()

def encrypt_image(image_path, key):
    """Encrypt the image."""
    # Open the image
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Encrypt the image data
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(image_data)

    # Save the encrypted image
    with open("encrypted_" + os.path.basename(image_path), "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_image(encrypted_image_path, key):
    """Decrypt the image."""
    # Open the encrypted image
    with open(encrypted_image_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the image data
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Save the decrypted image
    with open("decrypted_" + os.path.basename(encrypted_image_path), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ")
    if choice.lower() == 'e':
        image_path = input("Enter the path of the image to encrypt: ")
        key = generate_key()
        encrypt_image(image_path, key)
        print("Image encrypted successfully!")
    elif choice.lower() == 'd':
        encrypted_image_path = input("Enter the path of the encrypted image: ")
        key = load_key()
        decrypt_image(encrypted_image_path, key)
        print("Image decrypted successfully!")
    else:
        print("Invalid choice. Please choose 'e' or 'd'.")

if __name__ == "__main__":
    main()