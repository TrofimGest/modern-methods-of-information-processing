import cv2
from choosing_distribution import choosing_distribution


def random_change_color(img):
    number = choosing_distribution('uniform', 'color')

    color_spaces = ('RGB','GRAY','HSV','LAB','XYZ','YUV')

    change_color_image = cv2.cvtColor(img, getattr(cv2,'COLOR_BGR2' + color_spaces[number]))

    return change_color_image
