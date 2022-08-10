#!/usr/bin/env python3
import os
import re
from PIL import Image

im = Image.open("bridge.jpeg")
# im.rotate(180).show()


# new_im = im.resize((600,450))
# new_im.save("resized_bridge.jpeg")
# new_im.rotate(90).save("resized_bridge.jpeg")

# new_image = Image.open("New_images/ic_beenhere_white_48dp")
# new_image.rotate(-90).convert("RGB").resize((128,128)).save("Processed/practice_image.jpeg")


# entries = os.listdir('New_images/')
# for entry in entries:
#     print(entry)
#     im = Image.open("New_images/"+entry)
#     im.rotate(-90).convert("RGB").resize((128,128)).save("Processed/"+entry+".jpeg","JPEG",quality=100)

# os.getcwd()

yourpath = "New_images/"
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpeg"
        outfile=re.sub("New_images/","",outfile)
        try:
            im = Image.open(os.path.join(root, name))
            im.resize((128,128)).rotate(-90).convert("RGB").save("Processed/"+outfile, "JPEG", quality=100)
        except Exception as e:
            print (e)
print("Task done!")