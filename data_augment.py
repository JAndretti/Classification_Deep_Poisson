import Augmentor
import os
import shutil

print(Augmentor.__version__)

# Créez un objet "pipeline" avec votre jeu de données d'images
folder_paths = ['data/ange', 'data/clown','data/goldfish','data/lion','data/scalaire']

for folder in folder_paths:
    p = Augmentor.Pipeline(folder,output_directory = '')

    # Ajoutez des opérations de transformation au pipeline
    p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
        # Miroir horizontal
    p.flip_left_right(probability=0.5)

    # Miroir vertical
    p.flip_top_bottom(probability=0.5)

    # Changement de couleur
    p.random_color(probability=0.5, min_factor=0.8, max_factor=1.2)

    # Générez de nouvelles données en exécutant le pipeline
    sample = 1500-len(os.listdir(folder))
    if sample > 0:
        p.sample(sample)

