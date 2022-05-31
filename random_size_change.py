import cv2
from choosing_distribution import choosing_distribution

def random_resize(img):
    print('Original Dimensions : ',img.shape)

    devide = choosing_distribution('exponential', 'size') # percent of original size
    width = int(img.shape[1] / devide)
    height = int(img.shape[0] / devide)
    dim = (width, height)
  
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
    print('Resized Dimensions : ',resized.shape)
 
    return resized
