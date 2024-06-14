from cryptography.fernet import Fernet
import os

# Anahtarı okuma (txt formatında)
def load_key():
    return open("encryption_key.txt", "rb").read()

# Dosyaları çözme
def decrypt_files(key, file_paths):
    fernet = Fernet(key)
    for file_path in file_paths:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)

# Örnek dosyaları çözme işlemi
def example_decryption():
    key = load_key()

    # Şifrelenmiş dosya yolları
    files_to_decrypt = [
        "C:\\Users\\Kaan\\Desktop\\deneme\\deneme1.txt"
    ]

    decrypt_files(key, files_to_decrypt)
    print("Dosyalar başarıyla çözüldü.")

# Örnek dosyaları çözme işlemi
if __name__ == "__main__":
    example_decryption()
