import numpy as np
import cv2
import os

# Chemin du dossier à parcourir
folder_path = "dataSet"

# Créer le dossier "output" s'il n'existe pas déjà
output_folder = os.path.join(folder_path, 'output')
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    # Vérifie si le fichier est un fichier image
    if filename.endswith(".jpg"):
        y = 50
        x = 0
        h = 100
        w = 200
        image_path = os.path.join(folder_path, filename)
        # Vérifie si l'image peut être lue
        if os.path.isfile(image_path):
            image = cv2.imread(image_path)
            if image is not None:
                crop = image[y:y + h, x:x + w]
                # Enregistre l'image de sortie dans le dossier "output"
                output_path = os.path.join(output_folder, 'Output' + filename)
                cv2.imwrite(output_path, crop)


# chemin du dossier contenant les images
folder_path = "dataSet/output"

# créer un dossier pour stocker les images traitées
if not os.path.exists("treatment_dataSet"):
    os.mkdir("treatment_dataSet")

# parcourir toutes les images dans le dossier
for image_name in os.listdir(folder_path):
    # construire le chemin complet de l'image
    image_path = os.path.join(folder_path, image_name)

    # vérifier si le fichier existe
    if not os.path.isfile(image_path):
        print(f"Le fichier {image_name} n'existe pas!")
        continue

    # charger l'image en niveaux de gris
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # récupérer la hauteur et la largeur de l'image
    height, width = img.shape[:2]

    # parcourir tous les pixels de l'image
    for y in range(height):
        for x in range(width):
            # récupérer la valeur du pixel à l'emplacement (x, y)
            pixel_value = img[y, x]

            # si la valeur du pixel est supérieure à 220, le mettre en blanc (255)
            if pixel_value > 220:
                img[y, x] = 255
            # sinon, mettre le pixel en noir (0)
            else:
                img[y, x] = 0

    # enregistrer l'image modifiée dans le dossier treatment_dataSet
    output_path = os.path.join("treatment_dataSet", image_name)
    cv2.imwrite(output_path, img)

