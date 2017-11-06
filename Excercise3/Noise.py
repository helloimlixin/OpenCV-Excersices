"""
@author: xinli
Folders should be modified accordingly while running
"""

import cv2
import random
import numpy as np

def add_gaussian_noise(src,mean,sigma):
    noiseArr = src.copy()
    noiseArr = np.random.normal(mean,sigma,src.shape)
    np.add(src,noiseArr,src,casting="unsafe")
    return;
    
def add_salt_pepper_noise(img,pa,pb):
    row,col,ch=img.shape
    amount1=row*col*pa
    amount2=row*col*pb
    for i in range(int(amount1)):
        img[int(random.uniform(0,row))][int(random.uniform(0,col))]=0
    for i in range(int(amount2)):
        img[int(random.uniform(0,row))][int(random.uniform(0,col))]=255
        
    
original=cv2.imread('/Users/xinli/Downloads/OpenCV_homework/Test_images/baboon.jpg')
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/Original.jpg',original)

noise_img=original.copy()
mean=0
sigma=10
add_gaussian_noise(noise_img,mean,sigma)
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/Gaussian.jpg',noise_img)

noise_dst=cv2.blur(noise_img,(4,4))
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/Boxfilter.jpg',noise_dst)

noise_dst1=cv2.GaussianBlur(noise_img,(3,3),1.5)
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/GaussianBlurfilter.jpg',noise_dst1)

noise_dst2=cv2.medianBlur(noise_img,3)
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/Medianfilter.jpg',noise_dst2)

noise_img2 = original.copy()
add_salt_pepper_noise(original,0.2,0.2)
cv2.imwrite("/Users/xinli/Downloads/OpenCV_homework/Outputs_3/SaltandPeperNoise.jpg", noise_img2)

noise_dst3=cv2.blur(noise_img2,(4,4))
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/Boxfilter2.jpg',noise_dst3)

noise_dst4=cv2.GaussianBlur(noise_img2,(3,3),1.5)
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/GaussianBlurfilter2.jpg',noise_dst4)

noise_dst5=cv2.medianBlur(noise_img2,3)
cv2.imwrite('/Users/xinli/Downloads/OpenCV_homework/Outputs_3/Medianfilter2.jpg',noise_dst5)