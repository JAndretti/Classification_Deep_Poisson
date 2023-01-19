import Augmentor
import os

# Affiche la version d'Augmentor en cours d'utilisation
print(Augmentor.__version__)

def augment(folder_paths):

    # Pour chaque dossier de la liste folder_paths
    for folder in folder_paths:
        # Créez un objet "pipeline" en utilisant la fonction Augmentor.Pipeline() 
        # en spécifiant le chemin du dossier et l'emplacement de sortie pour les images générées.
        p = Augmentor.Pipeline(folder,output_directory = '')

        # Ajoutez des opérations de transformation au pipeline
        # Rotation avec une probabilité de 0.7 et une rotation maximale de 10 degrés à gauche et 10 degrés à droite
        p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
        # Zoom avec une probabilité de 0.5 et un facteur de zoom compris entre 1.1 et 1.5
        p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
        # Miroir horizontal avec une probabilité de 0.5
        p.flip_left_right(probability=0.5)

        # Miroir vertical avec une probabilité de 0.5
        p.flip_top_bottom(probability=0.5)

        # Changement de couleur avec une probabilité de 0.5 et un facteur de couleur compris entre 0.8 et 1.2
        p.random_color(probability=0.5, min_factor=0.8, max_factor=1.2)

        # Générez de nouvelles données en exécutant le pipeline
        # sample est le nombre d'images générées en soustraire le nombre d'images existantes dans le dossier de l'original.
        sample = 1500-len(os.listdir(folder))
        if sample > 0:
            p.sample(sample)
