import bcrypt
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# 1. Obtenez le mot de passe principal
master_password = input("Ana şifre girin: ").encode()

# 2. Créer du sel (doit être stocké dans l'application réelle !)
salt = os.urandom(16)

# 3. Dériver la clé avec PBKDF2HMAC
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100_000,
)

key = base64.urlsafe_b64encode(kdf.derive(master_password))
fernet = Fernet(key)

# 4. Données à crypter (par exemple, un mot de passe de site)
password_to_encrypt = input("Şifrelenecek veri: ").encode()

# 5. Cryptage
encrypted = fernet.encrypt(password_to_encrypt)
print(f"Şifrelenmiş veri: {encrypted.decode()}")

# 6. Analyse
decrypted = fernet.decrypt(encrypted)
print(f"Çözülmüş veri: {decrypted.decode()}")
