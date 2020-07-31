#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install opencv-python')


# In[ ]:


import cv2
import sys


# In[ ]:


image=cv2.imread("demon.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayImageInv = 255-grayImage
grayImageInv = cv2.GaussianBlur(grayImageInv, (61,61), 0) #adjust according to your need.
output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0) #adjust according to your need.
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", image)
cv2.imshow("pencilsketch", output)
cv2.imwrite("Output.jpg",output)
cv2.waitKey(0)
cv2.destroyAllWindows()

