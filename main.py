import cv2
from random_rotation import random_rotation
from random_change_color import random_change_color
from upload_photos import getNPhotos
from random_size_change import random_resize
from saving_photo import saving_photo
from img_on_img import random_img_on_img

from random import randint

# test = getNPhotos(5)
# start = 0
# end = 5
# for img in test:
#     if(start != end):
#         testImg = test[start]
#         currentImg = cv2.imread(testImg)
#         result = random_rotation(random_resize(random_change_color(currentImg)))
#         cv2.imshow("Result image", result)
#         cv2.waitKey(0)
#         name = randint(1,359)
#         isSave = saving_photo(result, str(name), 'jpg')
#         print(isSave)
#         start = start + 1


random_img_on_img('test/mem.jpg')

# print(test)
# img = cv2.imread(testImg)

# cv2.imshow("Origin image", img)
# cv2.waitKey(0)

# rotated = random_rotation(img)
# cv2.imshow("Rotated image", rotated)
# cv2.waitKey(0)

# resized = random_resize(img)
# cv2.imshow("Resizedimage", resized)
# cv2.waitKey(0)

# color = random_change_color(img)
# cv2.imshow("Changed color image", color)
# cv2.waitKey(0)

# result = random_rotation(random_resize(random_change_color(img)))
# cv2.imshow("Result image", result)
# cv2.waitKey(0)

# isSave = saving_photo(result, 'result123', 'jpg')
# print(isSave)
