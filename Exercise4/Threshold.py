
"""
@author: xinli
"""


import numpy as np
import cv2


original = cv2.imread('/Users/xinli/Downloads/OpenCV_homework/Test_images/baboon.jpg',1)

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs_4/Original.jpg", original)

threshold_value = 128
ret, thresh_trunc = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_TRUNC)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs_4/ThreshTrunc.jpg", thresh_trunc)

ret, thresh_binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs_4/ThreshBinary.jpg", thresh_binary)

ret, thresh_binary1 = cv2.threshold(gray, 27, 255, cv2.THRESH_BINARY)
ret, thresh_binary2 = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
band_threshold = thresh_binary1&thresh_binary2
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs_4/BandThreshold.jpg", band_threshold)

ret,semithreshold = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)
semithreshold = gray&semithreshold
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs_4/Semithreshold.jpg", semithreshold)

adaptive_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs_4/AdaptiveThresh.jpg", adaptive_thresh)