import pylab as pl	# imoprt matplotlib's subpackage as pl use for graph
import numpy as np	# use numpy library as np for array object
import cv2			# opencv-python
import scipy		# call math function, [scipy.hypot, scipy.arctan]
import math			# call math function, [math.pi]

###	Edge Linking-Edge tracking by hysteresis
def linking(i, j): # if pixel is an edge 
    for m in range(-1, 2): 		# count the pixel around [i, j]
        for n in range(-1, 2):	# count the pixel around [i, j]
            if M_above_high[i+m, j+n]==0 and M_above_low[i+m, j+n]!=0: # if the pixel around [i, j]'s value is between upper and lower bound
                M_above_high[i+m, j+n]=1 # set that pixel to be edge
                linking(i+m, j+n) 		 # do recursively to find next edge pixel
				
img_name = input('image name(with .jpg .png): ')	# input image name

threshold_prefer = input('image threshold values(1.Input 2.Auto(the program will calculate itself)): ') # input the threshold value
if (threshold_prefer == 1): 	 # if 1.input from keyboard
	min_VAL = input('min_VAL: ') # set min value
	max_VAL = input('max_VAL: ') # set max value


### read image and convert to grayscale
img = cv2.imread(img_name) # read image
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayscal
x, y = grayimg.shape # get image size x*y, a image with x rows and y columns

### Smooth image with Gaussian filter
Gimg = cv2.GaussianBlur(grayimg,(3, 3),0) # call opencv GaussianBlur function

Gnonimg = np.zeros((x, y), dtype = 'i')   # copy Gaussian image "Gimg" to "Gnonimg" inorder to avoid data overflow in image array
for i in range(0, x):					  # for-loop from row 0 to x
    for j in range(0, y):				  # for-loop from column 0 to y
        Gnonimg[i, j] = Gimg[i, j]		  # copy the image values

		
###	set first derivative in horizontal and vertical orientation. Find magnitude and orientation of gradient for each pixel
GX = np.ones((x, y), dtype = 'f')			# first derivative in horizontal orientation
GY = np.zeros((x, y), dtype = 'f')			# first derivative in vertical orientation
magnitude = np.zeros((x, y), dtype = 'f')	# magnitude of gradient
orientation = np.zeros((x, y), dtype = 'f')	# orientation of gradient

"""
### simple filter
for i in range(1, x-1): 	# set first derivative from 1 to x-1 (because of the edge of the image)
    for j in range(1, y-1): # set first derivative from 1 to y-1 (because of the edge of the image)
		GX[i, j]=(Gnonimg[i, j+1]-Gnonimg[i, j]+Gnonimg[i+1, j+1]-Gnonimg[i+1, j])  # simple filter in x diection
		GY[i, j]=(Gnonimg[i+1, j]-Gnonimg[i, j]+Gnonimg[i+1, j+1]-Gnonimg[i, j+1])  # simple filter in y diection
"""	
		
### Sobel filter	
for i in range(1, x-1): 	# set first derivative from 1 to x-1(because of the edge of the image)
    for j in range(1, y-1): # set first derivative from 1 to y-1(because of the edge of the image)
		GX[i, j]=((Gnonimg[i-1, j+1]-Gnonimg[i-1, j-1]+2*(Gnonimg[i, j+1]-Gnonimg[i, j-1])+Gnonimg[i+1, j+1]-Gnonimg[i+1, j-1])) # sobel filter in X diection
		GY[i, j]=((Gnonimg[i+1, j-1]-Gnonimg[i-1, j-1]+2*(Gnonimg[i+1, j]-Gnonimg[i-1, j])+Gnonimg[i+1, j+1]-Gnonimg[i-1, j+1])) # sobel filter in Y diection

		
magnitude = scipy.hypot(GX, GY) # calculate magnitude value of each pixel

# if GX == 0 then GX = 1, in order to avoid error when calculate orientation value 
for i in range(1, x-1): 
    for j in range(1, y-1):
        if GX[i,j]==0:
           GX[i,j]=1
       
orientation = scipy.arctan(GY/GX) # calculate orientation value of each pixel 

### transform orientation value to degree (orientation*180/pi), then clasify each pixel into 0, 45, 90 and 135 degree
for i in range(0, x):		# count pixel from 0 to x
    for j in range(0, y):	# count pixel from 0 to y
        orientation[i, j] = orientation[i, j]*180/math.pi # transform orientation into degree
        if orientation[i, j]<0: # tranform which degree < 0 to 0-360
            orientation[i, j] = orientation[i, j]+360 # if degree is negative +360 to become positive degree
        
		# classify every pixel
        if (orientation[i, j]<22.5 and orientation[i, j]>=0) or (orientation[i, j]>=157.5 and orientation[i, j]<202.5) or (orientation[i, j]>=337.5 and orientation[i, j]<=360):
               orientation[i, j]=0 # if 0<=degree<225 or 157.5<=degree<202.5 or 337.5<=degree<360 the pixel orientation = 0
        elif (orientation[i, j]>=22.5 and orientation[i, j]<67.5) or (orientation[i, j]>=202.5 and orientation[i, j]<247.5):
               orientation[i, j]=45 # if 22.5<=degree<67.5 or 202.5<=degree<247.5 the pixel orientation = 45
        elif (orientation[i, j]>=67.5 and orientation[i, j]<112.5)or (orientation[i, j]>=247.5 and orientation[i, j]<292.5):
               orientation[i, j]=90 # if 67.5<=degree<112.5 or 247.5<=degree<292.5 the pixel orientation = 90
        else: 
               orientation[i, j]=135 # if 112.5<=degree<157.5 or 292.5<=degree<337.5.5 the pixel orientation = 135
    
###	Non-maximum Suppression
for i in range(1, x-1):		# count pixel from 1 to x-1
    for j in range(1, y-1): # count pixel from 1 to y-1
        if orientation[i,j]==0: # if the pixel orientation = 0, compare with it's right and left pixel
            if (magnitude[i, j]<=magnitude[i, j+1]) or (magnitude[i, j]<=magnitude[i, j-1]): # if these pixel's magnitude are all bigger than magnitude[i,j]
                magnitude[i][j]=0 # set magnitude[i, j]=0
        elif orientation[i, j]==45: # if the pixel orientation = 45, compare with it's upper-right and lower-left pixel
            if (magnitude[i, j]<=magnitude[i-1, j+1]) or (magnitude[i, j]<=magnitude[i+1, j-1]): # if these pixel's magnitude are all bigger than magnitude[i,j]           
                magnitude[i, j]=0 # set magnitude[i, j]=0
        elif orientation[i, j]==90: # if the pixel orientation = 90, compare with it's upper and lower pixel
            if (magnitude[i, j]<=magnitude[i+1, j]) or (magnitude[i, j]<=magnitude[i-1, j]): # if these pixel's magnitude are all bigger than magnitude[i,j]  
                magnitude[i, j]=0 # set magnitude[i, j]=0
        else: # if the pixel orientation = 135, compare with it's lower-right and upper-left pixel
            if (magnitude[i, j]<=magnitude[i+1, j+1]) or (magnitude[i, j]<=magnitude[i-1, j-1]): # if these pixel's magnitude are all bigger than magnitude[i,j]  
                magnitude[i, j]=0 # set magnitude[i, j]=0

###	Hysteresis Thresholding (Canny recommended a upper:lower ratio between 2:1 and 3:1.)
m = np.max(magnitude) # find the largest pixel to be the parameter of the threshold

### upper:lower ratio between 2:1 and 3:1
if (threshold_prefer == 2): # if threshold prefer is auto 
	max_VAL = 0.2*m  		# set upper bound
	min_VAL = 0.1*m  		# set lower bound

	"""
	max_VAL = 0.3*m  		# set upper bound
	min_VAL = 0.1*m  		# set lower bound
	"""

M_above_high=np.zeros((x,y), dtype='f') # initial the table with pixel value above upper bound are sure to be edges
M_above_low=np.zeros((x,y), dtype='f')  # initial the table with pixel value above lower bound, 
									    # the pixel thich below the lower bound are sure to be non-edges

# fill the pixel value in "M_above_high" and "M_above_low"
for i in range(0, x):							 # count image pixel from 0 to x
    for j in range(0, y):						 # count image pixel from 0 to y
        if magnitude[i,j]>=max_VAL: 			 # if pixel magnitude value > upper bound
            M_above_high[i,j] = magnitude[i,j]	 # store to M_above_high
        if magnitude[i,j]>=min_VAL:				 # if pixel magnitude value > lower bound
            M_above_low[i,j] = magnitude[i,j]	 # store to M_above_low
       

M_above_low = M_above_low - M_above_high # calculte the magnitude value which are less than uper bound and greater than lower bound
										 # These are classified edges or non-edges based on their connectivity

for i in range(1, x-1): 		# count pixel in M_above_high
    for j in range(1, y-1): 	# count pixel in M_above_high
        if M_above_high[i,j]: 	# if the pixel's value is greater than upper bound
            M_above_high[i,j]=1 # set [i,j] is an edge = 1
            linking(i, j) 		# call finction to find next edge pixel around [i, j]

pl.subplot(121)				# image position
pl.imshow(grayimg)			# show image "grayimg"
pl.title('gray image')		# graph title "gray image"
pl.set_cmap('gray')			# show in gray scale

pl.subplot(122)				# image position
pl.imshow(M_above_high)		# show image "M_above_high"
pl.title('edge image')		# graph title "edge image"
pl.set_cmap('gray')			# show in gray scale

pl.show()	                # output image