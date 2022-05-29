from PIL import Image
from random import randint

# pip install Pillow

def random_img_on_img(paste_image_path):

    devideOn = randint(4,10)
    pasteImgNumber = randint(5, 10)
    backgoundNumber = randint(1, 10)
    
    img_paste = Image.open(paste_image_path)
    img_bg = Image.open('backgrounds/' + str(backgoundNumber) + '.jpg')

    bd_width, bd_height = img_bg.size

    fixed_width = int(bd_width/devideOn)

    width_percent = (fixed_width / float(img_paste.size[0]))

    height_size = int((float(img_paste.size[0]) * float(width_percent)))

    # меняем размер на полученные значения
    new_image = img_paste.resize((fixed_width, height_size))

    new_paste_width, new_paste_height = new_image.size

    back_im = img_bg.copy()

    i = 0
    while i < pasteImgNumber:
        random_width = randint(0, bd_width - new_paste_height)
        random_height = randint(0, bd_height - new_paste_width)
        back_im.paste(new_image, (random_width,random_height))
        i = i + 1


    back_im.save('res.jpg')

    img_paste.close()
    img_bg.close()