"""
@author: xinli
Folder paths should be modified accordingly when running
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

# Print out corresponding values of pixels
print("R: "+ str(R[20,25]))
print("G: "+ str(G[20,25]))
print("B: "+ str(B[20,25]))
print("Y: "+ str(Y[20,25]))
print("Cb: "+ str(Cb[20,25]))
print("Cr: "+ str(Cr[20,25]))
print("H: "+ str(H[20,25]))
print("S: "+ str(S[20,25]))
print("V: "+ str(V[20,25]))
