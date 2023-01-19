import os
import numpy as np
import cv2 



def redim(poisson):


    os.mkdir('new_data')
    for fish in poisson:
        os.mkdir('new_data/'+fish)

    #Définir le nouveau chemin pour stocker les images redimensionnées
    new_path = 'new_data/'
    print(poisson)

    # Pour chaque poisson dans la liste
    for folder_path in poisson:
        # Récupérer la liste de tous les fichiers jpg dans le dossier correspondant de "data"
        file_list = os.listdir('data/'+folder_path)

        # Pour chaque fichier dans la liste
        for i, file_name in enumerate(file_list):
            if(os.path.splitext(file_name)[1]=='.jpg'):

        # Charger l'image en utilisant cv2.imread()
                image = cv2.imread('data/'+folder_path+'/'+file_name)
                if image is None:
                    print("bug")

                # Redimensionnement de l'image en utilisant cv2.resize() à une taille de 100x100
                new_image = cv2.resize(image, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)

                # vérifier si l'image existe déjà dans le nouveau dossier de sortie
                if not os.path.exists(new_path + '/' + file_name):
                    # Enregistrer l'image redimensionnée dans le nouveau dossier de sortie
                    cv2.imwrite(new_path+folder_path+'/'+file_name, new_image)

    # Initialiser le compteur de fichiers à 0
    num_files = 0

    # Parcourir le répertoire "new_data" et compter les fichiers
    for root, dirs, files in os.walk(new_path):
        num_files += len(files)

    #afficher le nombre de fichiers final
    print(f'Le répertoire contient {num_files} fichiers.')
