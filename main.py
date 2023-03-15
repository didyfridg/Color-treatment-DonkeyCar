import cv2
import os

# variable du crop
y = 50
x = 0
h = 100
w = 200



folder_path = "dataSet"

output_folder = os.path.join(folder_path, 'output')
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        image_path = os.path.join(folder_path, filename)
        if os.path.isfile(image_path):
            image = cv2.imread(image_path)
            if image is not None:
                crop = image[y:y + h, x:x + w]
                output_path = os.path.join(output_folder, 'Output' + filename)
                cv2.imwrite(output_path, crop)

folder_path = "dataSet/output"

if not os.path.exists("treatment_dataSet"):
    os.mkdir("treatment_dataSet")

for image_name in os.listdir(folder_path):
    image_path = os.path.join(folder_path, image_name)

    if not os.path.isfile(image_path):
        print(f"Le fichier {image_name} n'existe pas!")
        continue

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    height, width = img.shape[:2]

    for y in range(height):
        for x in range(width):
            pixel_value = img[y, x]

            # si la valeur du pixel est supérieure à 200, le mettre en blanc (255)
            if pixel_value > 200:
                img[y, x] = 255
            # sinon, mettre le pixel en noir (0)
            else:
                img[y, x] = 0

    output_path = os.path.join("treatment_dataSet", image_name)
    cv2.imwrite(output_path, img)

