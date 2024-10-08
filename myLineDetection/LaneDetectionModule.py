import cv2
import numpy as np
import utlis


def getLaneCurve(img):
    imgThres = utlis.thresholding(img)
    cv2.imshow('Threshold', imgThres)
    return None



if __name__ == '__main__':
    print(cv2.__version__)
    cap = cv2.VideoCapture('vid1.mp4')
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        getLaneCurve(img)
        cv2.imshow('Video Miaad', img)
        cv2.waitKey(1)