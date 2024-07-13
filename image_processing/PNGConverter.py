import os
import sys
from PIL import Image

# Before running this code make sure the folder containing the images you want to convert are in the same directory as this code file. Make sure your terminal is also pointing to the directory as well.

image_folder = sys.argv[1] + "/"
target_folder = sys.argv[2] + "/"

if not os.path.exists(target_folder):
    os.mkdir(target_folder)
    
for file in os.listdir(image_folder):
    clean_name = os.path.splitext(file)[0]
    
    try:
        with Image.open(image_folder + file) as im:
             im.save(f'{target_folder}{clean_name}.png')
    except OSError:
        print("cannot convert", file)