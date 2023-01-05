import os

# Définir la liste des chemins des dossiers contenant les photos
folder_paths = ['data/ange', 'data/clown','data/goldfish','data/lion','data/scalaire']

# Pour chaque dossier de la liste
for folder_path in folder_paths:
  # Récupérer le nom du dossier
  folder_name = os.path.basename(folder_path)

  # Récupérer la liste de tous les fichiers dans le dossier
  file_list = os.listdir(folder_path)
  print(len(file_list))

  # Pour chaque fichier dans la liste
  for i, file_name in enumerate(file_list):
    # Générer un nouveau nom de fichier en utilisant le nom du dossier, l'index de l'itération et l'extension de fichier originale
    new_filename = '{}{}.{}'.format(folder_name, i, file_name.split('.')[-1])

    # Construire le chemin du fichier d'origine et du fichier de destination
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_filename)
    if not os.path.exists(new_file_path):
    # Renommer le fichier en utilisant le chemin de destination
      os.rename(old_file_path, new_file_path)

