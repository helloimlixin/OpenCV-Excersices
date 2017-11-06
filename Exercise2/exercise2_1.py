#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:07:23 2017

@author: xinli
"""

import cv2
import numpy as np

original = cv2.imread("/Users/xinli/Downloads/OpenCV_homework/Test_images/baboon.jpg")
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/Original.jpg", original)

#RGB
# note that the original order here should be BGR instead of RGB
B,G,R = cv2.split(original)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/R.jpg",R)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/G.jpg",G)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/B.jpg",B)


# Lumina
Y,Cb,Cr = cv2.split(cv2.cvtColor(original,cv2.COLOR_BGR2YCR_CB))
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/Y.jpg",Y)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/Cb.jpg",Cb)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/Cr.jpg",Cr)

# HSV
H,S,V = cv2.split(cv2.cvtColor(original,cv2.COLOR_BGR2HSV))
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/H.jpg",H)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/S.jpg",S)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs/V.jpg",V)
