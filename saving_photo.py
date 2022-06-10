import cv2
import os
from random import randint


def saving_photo(photos):

    photosPath = './photos'
    isExist = os.path.exists(photosPath)
    if not isExist:
        os.makedirs(photosPath)

    for photo in photos:
        randNum = random_with_N_digits(3)
        name = 'savedPhoto#' + str(randNum) + '.jpg'
        while(True):
            if(nameExists('./photos/' + str(name))):
                randNum = random_with_N_digits(3)
                name = 'savedPhoto#' + str(randNum) + '.jpg'
            else:
                status = cv2.imwrite('./photos/' + str(name), photo)
                print("Image written to file-system : ", status)
                break


def nameExists(name):
    return os.path.exists(name)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
