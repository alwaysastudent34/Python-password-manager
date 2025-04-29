import bcrypt
import base64
import os
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# 1. Obtenez le mot de passe maître
master_password = input("Entrez le mot de passe maître : ").encode()

# 2. Vérifiez le fichier salt (lire s'il existe, créer s'il n'existe pas)
if os.path.exists("salt.bin"):
    with open("salt.bin", "rb") as f:
        salt = f.read()
else:
    salt = os.urandom(16)
    with open("salt.bin", "wb") as f:
        f.write(salt)

# 3. Dériver la clé avec PBKDF2HMAC
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100_000,
)

key = base64.urlsafe_b64encode(kdf.derive(master_password))
fernet = Fernet(key)

# 4. Ajout d'un mot de passe à chiffrer
password_to_encrypt = input("Entrez le mot de passe à chiffrer : ").encode()
encrypted = fernet.encrypt(password_to_encrypt)

# 5. Stocker le mot de passe chiffré dans un fichier
with open("passwords.json", "w") as f:
    json.dump({"encrypted": encrypted.decode()}, f)

print(f"Mot de passe chiffré enregistré : {encrypted.decode()}")

# 6. Lire et déchiffrer le mot de passe du fichier
with open("passwords.json", "r") as f:
    data = json.load(f)

encrypted_from_file = data["encrypted"].encode()
decrypted = fernet.decrypt(encrypted_from_file)
print(f"Mot de passe déchiffré depuis le fichier : {decrypted.decode()}")
