 What is this project?

This project is a simple password manager that stores your passwords securely.
It uses a master password to protect access and AES encryption to keep passwords safe.
 Main Features

    Master password authentication

    Encrypt and decrypt passwords with Fernet (AES)

    Save passwords to a local JSON file

    Simple command-line menu

 Requirements

    Python 3

    cryptography


To install dependencies:

pip install cryptography

 How to run

python password_manager.py


Then follow the menu:

    Show saved passwords

    Add a new password

    Exit

 Note

Your master password is used to create a unique encryption key.
If you forget it, your saved passwords cannot be decrypted.



#################################################  VERSION FRANCAISE  #############################################################################################

 C’est quoi ce projet ?

Ce projet est un gestionnaire de mots de passe simple.
Il protège vos mots de passe avec un mot de passe maître et les chiffre avec AES (Fernet).
 Fonctions principales

    Authentification avec mot de passe maître

    Chiffrement et déchiffrement des mots de passe

    Sauvegarde des mots de passe dans un fichier JSON local

    Menu interactif dans le terminal

 Prérequis

    Python 3

    cryptography


Installer les dépendances :

pip install cryptography

 Comment l’exécuter ?

python password_manager.py

Puis, suivez le menu :

    Afficher les mots de passe

    Ajouter un mot de passe

    Quitter

 Attention

Le mot de passe maître sert à générer une clé unique de chiffrement.
Si vous l’oubliez, vous ne pourrez plus lire vos mots de passe enregistrés.




