from data_augment import augment
from script_rename import rename
from script_redimensionne import redim


folder_paths = ['data/ange', 'data/clown','data/goldfish','data/lion','data/scalaire','data/guppys','data/platys','data/discus','data/papillons','data/perroquets','data/kois'] 
augment(folder_paths)
rename(folder_paths)
#liste des poissons
poisson = ['ange', 'clown','goldfish','lion','scalaire','guppys','platys','discus','papillons','perroquets','kois']
redim(poisson)
