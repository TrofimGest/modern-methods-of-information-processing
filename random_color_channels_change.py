import cv2
from choosing_distribution import choosing_distribution


def random_color_channels_change(img):

    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    r, g, b = cv2.split(img2)

    r = r + choosing_distribution('exponential', 'rotation')

    g = g + choosing_distribution('normal', 'rotation')

    b = b + choosing_distribution('uniform', 'rotation')

    color_channels_change = cv2.merge([r, g, b])

    return color_channels_change
