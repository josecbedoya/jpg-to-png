import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]  

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

success = True 

for filename in os.listdir(image_folder):
    try:
        img = Image.open(os.path.join(image_folder, filename))
        clean_name = os.path.splitext(filename)[0]
        img.save(os.path.join(output_folder, f"{clean_name}.png"), 'png')
    except Exception as e:
        print(e)
        success = False 

if success:
    print("done!")
