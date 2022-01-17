import sys
import os

import cv2 as cv
import numpy as np

cap = cv.VideoCapture
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


hsv_min = np.array([0,64,0])
hsv_max = np.array([30,255,255])
#mask1 = cv2.inRange(hsv, hsv_min, hsv_max)



