from PIL import Image
from random import randint

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
        devideOn = randint(4,10)
        fixed_width = int(bd_width/devideOn)

        width_percent = (fixed_width / float(img_paste.size[0]))

        height_size = int((float(img_paste.size[0]) * float(width_percent)))

        # меняем размер на полученные значения
        new_image = img_paste.resize((fixed_width, height_size))

        new_paste_width, new_paste_height = new_image.size
        
        if(i==0):
            x=0
            y=0
        else:
            x = x + round(kx)
            y = y + round(ky)

        back_im.paste(new_image, (x,y))

        i = i + 1


    back_im.save('res.jpg')

    img_paste.close()
    img_bg.close()