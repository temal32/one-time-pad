import os

def encrypt(filename):
    try:
        to_encrypt = open(filename, "rb").read()
        size = len(to_encrypt)
        key = os.urandom(size)
        with open(filename + ".key", "wb") as key_out:
            key_out.write(key)
        encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)
    except Exception as encrypt_error:
        print("Error occured while encrypting, " + encrypt_error)

def decrypt(filename, key):
    try:
        file = open(filename, "rb").read()
        key = open(key, "rb").read()
        decrypted = bytes(a ^ b for (a, b) in zip(file, key))
        with open("d_" + filename, "wb") as decrypted_out:
            decrypted_out.write(decrypted)
    except Exception as decrypt_error:
        print("Error occured while decrypting, " + decrypt_error)

filename = input("Enter file name: ")
choice = input("Encrypt or decrypt? (e/d): ")

if choice == "e":
    encrypt(filename)
elif choice == "d":
    decrypt(filename, filename + ".key")
else:
    print("Invalid input")
