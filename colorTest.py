import cv2
import os

# chemin du dossier contenant les images
folder_path = "imagesimdonkeycar/output"

# créer un dossier pour stocker les images traitées
if not os.path.exists("output_color"):
    os.mkdir("output_color")

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

    # vérifier si l'image a été chargée avec succès
    if img is None:
        print(f"Impossible de lire l'image {image_name}!")
        continue

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

    # enregistrer l'image modifiée dans le dossier output_color
    output_path = os.path.join("output_color", image_name)
    cv2.imwrite(output_path, img)

