# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hhcZX5uaBIZahQahkLz1Jav3y3WTaund
"""
#your code here
import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow    
from skimage import io
from PIL import Image
import matplotlib.pylab as plt

url = "https://drive.google.com/uc?export=view&id=1GgeG0KAJdj6wQddI2J_BwfPa-DdutA_D"

image = io.imread(url)
image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)#image numpy array
cv2_imshow(image_2)
data = Image.fromarray(image_2)
data.save('duck.png')
im = Image.open(r'duck.png') #image PIL object
im
pot=im.copy()
pot.resize((1,1))
colors = pot.getpixel((0,0))
pot
print(colors)
import matplotlib.image as img
import statistics
#duck1 = img.imread('1.jpeg')
x=duckf
#print(x)
#print(x.shape)
#x.resize((193,261,3))#actual size
R,G,B,RGB,r,g,b=0,0,0,[],[],[],[]
#print(x[192][260][0])
for i in range(0,192):
  for j in range(0,260):
    R+=x[i][j][0]
    r.append(x[i][j][0])
RGB.append((R/(193*261)+0.5)//1)
for i in range(0,192):
  for j in range(0,260):
    G+=x[i][j][1]
    g.append(x[i][j][1])
RGB.append((G/(193*261)+0.5)//1)
for i in range(0,192):
  for j in range(0,260):
    B+=x[i][j][2]
    b.append(x[i][j][2])
RGB.append((B/(193*261)+0.5)//1)
print("The Mean Color value (RGB) in the given image is",RGB)
#y=[1,2,3]
RGB1=[statistics.mode(r),statistics.mode(g),statistics.mode(b)]
print("The Mode Color value (RGB) in the given image is",RGB1 )

"""https://drive.google.com/file/d/1GgeG0KAJdj6wQddI2J_BwfPa-DdutA_D/view?usp=sharing"""
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb
import cv2
what1,what2,what3=(53, 142, 222)#(53, 142, 222) Mean Color value (RGB) in the given image is [108.0, 128.0, 96.0] The Mode Color value (RGB) in the given image is [0, 154, 31]
duckf = imread('duck.png')
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(duckf);
#print(duckf)
red_filtered = (abs(duckf[:,:,0] - what1)<100) & (abs(duckf[:,:,1]-what2)<100) & (abs(duckf[:,:,2]-what3)<100)
plt.figure(num=None, figsize=(8, 6), dpi=80)
duckf_new = duckf.copy()
duckf_new[:, :, 0] = duckf_new[:, :, 0] * red_filtered
duckf_new[:, :, 1] = duckf_new[:, :, 1] * red_filtered
duckf_new[:, :, 2] = duckf_new[:, :, 2] * red_filtered
imshow(duckf_new)