import PIL
from PIL import Image
import os
my_width = 1280
source_dir='D:/Source'
destination_dir='D:/Destination'


def img_Compressor(old_img, new_img,my_width):
    my_img = Image.open(old_img)
    width_Per = (my_width/float(my_img.size[0]))
    height_Size = int((float(my_img.size[1]) * float(width_Per)))
    newer_img = my_img.resize((my_width, height_Size), PIL.Image.ANTIALIAS)
    newer_img.save(new_img)


def all_Dir(source_dir, destination_dir ,width):
    files=os.listdir(source_dir)
    i=0
    for file in files:
        i+=1
        old_img=source_dir+ '/' +file
        new_img=destination_dir+ '/'+ file
        img_Compressor(old_img,new_img,width)
        print('Images',i)
all_Dir(source_dir,destination_dir,my_width)

