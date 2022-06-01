from PIL import Image
from random import randint
from saving_photo import saving_photo
from random_rotation import random_rotation
from random_change_color import random_change_color
from upload_photos import getNPhotos
from random_size_change import random_resize
from saving_photo import saving_photo
import os
import cv2

# pip install Pillow

def random_img_on_img(paste_image_path):

    pasteImgNumber = randint(5, 10)
    backgoundNumber = randint(1, 10)
    
    img_paste = Image.open(paste_image_path)
    img_bg = Image.open('backgrounds/' + str(backgoundNumber) + '.jpg')

    bd_width, bd_height = img_bg.size

    kx = bd_width/pasteImgNumber
    ky = bd_height/pasteImgNumber

    back_im = img_bg.copy()

    i = 0
    while i < pasteImgNumber:

        currentImg = cv2.imread(paste_image_path)
        result = random_rotation(random_resize(random_change_color(currentImg)))
        cv2.imwrite('res1.jpg', result)
        img_paste = Image.open('res1.jpg')

        devideOn = randint(4,10)
        fixed_width = int(bd_width/devideOn)

        width_percent = (fixed_width / float(img_paste.size[0]))

        height_size = int((float(img_paste.size[0]) * float(width_percent)))

        # меняем размер на полученные значения
        new_image = img_paste.resize((fixed_width, height_size))

        # new_paste_width, new_paste_height = new_image.size
        
        if(i==0):
            x=0
            y=0
        else:
            x = x + round(kx)
            y = y + round(ky)

        back_im.paste(new_image, (x,y))

        os.remove('res1.jpg')

        i = i + 1

    back_im.save('res.jpg')

    img = cv2.imread('res.jpg')
    
    saving_photo([img])

    os.remove('res.jpg')

    img_paste.close()
    img_bg.close()