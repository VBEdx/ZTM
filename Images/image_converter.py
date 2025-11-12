import sys
import os
from PIL import Image

# get the old folder and new folder
old_folder, new_folder = sys.argv[1], sys.argv[2]

# check if folders exists
if not os.path.exists(new_folder):
    os.makedirs(new_folder)


# convert files to png
# save to new folder
for file in os.listdir(old_folder):
    with Image.open(os.path.join(old_folder, file)) as img:
        img.save(fr"{new_folder}\{os.path.splitext(file)[0]}.png", format='png')

print('All done')






