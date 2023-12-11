import json
import hashlib
import getpass
import os

# Fonction pour hacher un mot de passe
def hash_password(password):
   sha256 = hashlib.sha256()
   sha256.update(password.encode())
   return sha256.hexdigest()

# Fonction pour ajouter un mot de passe
def add_password(website, password):
   # Vérifiez si passwords.json existe
   if not os.path.exists('passwords.json'):
       # Si passwords.json n'existe pas, initialisez-le avec une liste vide
       data = []
   else:
       # Chargez les données existantes depuis passwords.json
       try:
           with open('passwords.json', 'r') as file:
               data = json.load(file)
       except json.JSONDecodeError:
           # Gérez le cas où passwords.json est vide ou un JSON invalide.
           data = []
   # Hachez le mot de passe
   hashed_password = hash_password(password)
   # Créez un dictionnaire pour stocker le site web et le mot de passe
   password_entry = {'website': website, 'password': hashed_password}
   data.append(password_entry)
   # Enregistrez la liste mise à jour dans passwords.json
   with open('passwords.json', 'w') as file:
       json.dump(data, file, indent=4)

# Fonction pour récupérer un mot de passe enregistré
def get_password(website):
   # Vérifiez si passwords.json existe
   if not os.path.exists('passwords.json'):
       return None
   # Chargez les données existantes depuis passwords.json
   try:
       with open('passwords.json', 'r') as file:
           data = json.load(file)
   except json.JSONDecodeError:
       data = []
   # Parcourez tous les sites web et vérifiez si le site web demandé existe.
   for entry in data:
       if entry['website'] == website:
           # Retournez le mot de passe
           return entry['password']
   return None

# Boucle infinie pour garder le programme en cours d'exécution jusqu'à ce que l'utilisateur choisisse de quitter.
while True:
   print("1. Ajouter un mot de passe")
   print("2. Récupérer un mot de passe")
   print("3. Quitter")
   choice = input("Entrez votre choix: ")
   if choice == '1': # Si l'utilisateur veut ajouter un mot de passe
       website = input("Entrez le site web: ")
       password = getpass.getpass("Entrez le mot de passe: ")
       add_password(website, password)
       print("\n[+] Mot de passe ajouté!\n")
   elif choice == '2': # Si l'utilisateur veut récupérer un mot de passe
       website = input("Entrez le site web: ")
       saved_password = get_password(website)
       if saved_password:
           print(f"\n[+] Mot de passe pour {website}: {saved_password}\n")
       else:
           print("\n[-] Mot de passe non trouvé! Avez-vous enregistré le mot de passe?\n")
   elif choice == '3': # Si l'utilisateur veut quitter le gestionnaire de mots de passe
       break
