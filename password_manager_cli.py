import bcrypt
import base64
import os
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# Vérifiez le fichier salt
def get_salt():
    if os.path.exists("salt.bin"):
        with open("salt.bin", "rb") as f:
            return f.read()
    else:
        salt = os.urandom(16)
        with open("salt.bin", "wb") as f:
            f.write(salt)
        return salt

# Dériver la clé
def derive_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password))

# Charger la base de données de mots de passe
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            return json.load(f)
    return {}

# Enregistrer la base de données de mots de passe
def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

# Menu CLI
def main():
    master_password = input("Entrez le mot de passe maître : ").encode()
    salt = get_salt()
    key = derive_key(master_password, salt)
    fernet = Fernet(key)

    passwords = load_passwords()

    while True:
        print("\n--- Gestionnaire de Mots de Passe ---")
        print("1. Afficher les mots de passe")
        print("2. Ajouter un nouveau mot de passe")
        print("3. Quitter")
        choice = input("Votre choix : ")

        if choice == "1":
            if passwords:
                print("\nMots de passe enregistrés :")
                for name, enc_pass in passwords.items():
                    try:
                        decrypted = fernet.decrypt(enc_pass.encode()).decode()
                        print(f"{name} : {decrypted}")
                    except Exception as e:
                        print(f"{name} : (impossible à déchiffrer)")
            else:
                print("Aucun mot de passe enregistré.")
        elif choice == "2":
            name = input("Nom du mot de passe (ex : Gmail) : ")
            new_password = input("Mot de passe : ").encode()
            encrypted = fernet.encrypt(new_password).decode()
            passwords[name] = encrypted
            save_passwords(passwords)
            print("Mot de passe enregistré !")
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
