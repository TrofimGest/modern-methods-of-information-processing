import cv2


def get_outline(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('Binary image', thresh)
    cv2.waitKey(0)

    # detect the contours on the binary image
    contours, hierarchy = cv2.findContours(
        thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(image=image, contours=contours, contourIdx=-1,
                     color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow('Outline', image)
    cv2.waitKey(0)

    return image
