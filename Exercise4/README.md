This is the file folder for Exercise 4. 

# Question 1
Look at Threshold.cpp and implement the code in Python, and observe the results for different threshold values. Comment on the results.

# Answer 1
For adaptive thresholding, the output image is brighter than the original one, while for binary and band thresholding, more pixels are forced to 0 and 255, which results in black&white images. For a thresholded image, we can see pixels are truncated. 

# Question 2
What are the disadvantages of binary threshold?

# Answer 2
The major deficiency of binary thresholding is just mentioned above, which is to push the pixels to the two limit values (0 and 255), resulting in black and white images. 

# Question 3
When is Adaptive Threshold useful?

# Answer 3
For images with multiple regions with different degree of illumination, adaptive threshold can produce a satisfying result. 
