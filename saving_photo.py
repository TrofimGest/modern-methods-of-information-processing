import cv2
import os


def saving_photo(img, newImgName, format):

    photosPath = './photos'
    isExist = os.path.exists(photosPath)
    if not isExist:
        os.makedirs(photosPath)

    newPath = './photos/' + newImgName + '.' + format

    status = cv2.imwrite(newPath, img)

    print("Image written to file-system : ", status)

    return status
