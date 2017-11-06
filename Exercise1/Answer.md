# Question 1:
How does a program read the cvMat object, in particular, what is the
order of the pixel structure?

# Answer:
Matrix elements are stored row by row. Element (i, j) (i - 0-based row index, j - 0-based column index) of a matrix can be retrieved or modified using CV_MAT_ELEM macro:
```
uchar pixval = CV_MAT_ELEM(grayimg, uchar, i, j)
CV_MAT_ELEM(cameraMatrix, float, 0, 2) = image.width*0.5f;
```
To access multiple-channel matrices, you can use CV_MAT_ELEM(matrix, type, i, j*nchannels + channel_idx).

Internally, the cvMat structure is given by:
```
union {
   int   height
 
   int   rows
 
}; 	
 
union {
   int   cols
 
   int   width
 
}; 	
 
union {
   double *   db
 
   float *   fl
 
   int *   i
 
   uchar *   ptr
 
   short *   s
 
} 	data
 
int 	hdr_refcount
 
int * 	refcount
 
int 	step
 
int 	type
 
```

Thus the order of the pixel structure is given by bit depth, which can be 8, 16, 32 or 64 bits. The general format is given by CV_(S|U|F)C, where S means signed integer, U means unsigned integer and F means floating point (decimal values). You can have any number of channels (the number of data in each pixel).


