import cv2

param1 = 100
param2 = 10
white = [255, 255, 255]
thickness = 1


def get_outline(image, blackBackground):

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, param1, param1, cv2.THRESH_BINARY)

    # detect the contours on the binary image
    contours, hierarchy = cv2.findContours(
        thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(image=blackBackground, contours=contours, contourIdx=-1,
                     color=white, thickness=thickness, lineType=cv2.LINE_AA)

    cv2.imshow('Outline', blackBackground)
    cv2.waitKey(0)

    return blackBackground
