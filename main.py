import cv2
from random_rotation import random_rotation
from random_change_color import random_change_color
from upload_photos import getNPhotos
from random_size_change import random_resize
from saving_photo import saving_photo
from img_on_img import random_img_on_img
from get_outline import get_outline

test = getNPhotos(6)
start = 0
end = len(test)
photos = []
print(test)

for img in test:
    if(start != end):
        testImg = test[start]
        currentImg = cv2.imread(testImg)
        result = random_rotation(random_resize(random_change_color(currentImg)))
        cv2.imshow("Result image", result)
        cv2.waitKey(0)
        photos.append(result)
        start = start + 1

saving_photo(photos)

random_img_on_img(test[4])
# random_img_on_img('test/mem.jpg')

# img = cv2.imread('test/mem2.jpg')
# bg = cv2.imread('backgrounds/blackBackground.jpg')
# bg_result = get_outline(img, bg)
# saving_photo([bg_result])

# доделать весь функционал
