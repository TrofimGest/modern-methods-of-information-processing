import cv2
from random import randint

def random_rotation(img):
    # получим размеры изображения для поворота
    # и вычислим центр изображения
    (height,width) = img.shape[:2]
    center = (width/2, height/2)

    angle = randint(1,359)

    # повернем изображение на 180 градусов
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (width, height))
    # cv2.imshow("Rotated image", rotated)
    # cv2.waitKey(0)
    return rotated

# исправление пул реквеста