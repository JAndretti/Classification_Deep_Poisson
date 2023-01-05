import os
import numpy as np
import cv2 




poisson = ['ange', 'clown','goldfish','lion','scalaire']
try: 
    os.mkdir('new_data')
    for poisson in poisson:
        os.mkdir('new_data/'+poisson)
except OSError:
    pass  # Le dossier existe déjà, on ignore l'exception


# Définir la liste des chemins des dossiers contenant les photos
#folder_paths = ['data/ange', 'data/clown','data/goldfish','data/lion','data/scalaire']
new_path = 'new_data/'

# Pour chaque dossier de la liste
for folder_path in poisson:

    # Récupérer la liste de tous les fichiers dans le dossier
    file_list = os.listdir('data/'+folder_path)

    # Pour chaque fichier dans la liste
    for i, file_name in enumerate(file_list):
        if(os.path.splitext(file_name)[1]=='.jpg'):

    # Charger l'image en utilisant la librairie image de votre choix
            image = cv2.imread('data/'+folder_path+'/'+file_name)
            if image is None:
                print("bug")
        # Obtenir les dimensions de l'image


            new_image = cv2.resize(image, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)

            if not os.path.exists(new_path + '/' + file_name):
        # Enregistrer l'image redimensionnée
                cv2.imwrite(new_path+folder_path+'/'+file_name, new_image)

# Initialiser le compteur de fichiers à 0
num_files = 0

# Parcourir le répertoire et compter les fichiers
for root, dirs, files in os.walk(new_path):
    num_files += len(files)

print(f'Le répertoire contient {num_files} fichiers.')
