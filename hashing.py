import bcrypt


password = input("Donne un chiffre").encode('utf-8')

hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

print(f"Hash chiffre:{hashed_password.decode()}")


#####

verify_password = input("Répéter le mot de passe:").encode('utf-8')

if bcrypt.checkpw(verify_password, hashed_password):
    print("Mot de passe vérifié!")
else:
    print("Le mot de passe est incorrect.")