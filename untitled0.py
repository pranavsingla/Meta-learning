# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10VtgGA3aJ1otbvQEoKTNKaxZPtRAjWLB
"""

import numpy as np
import matplotlib.pyplot as plt
#print("hello")
a= np.zeros((100,50))
#final= np.ones((100,50))
number_ones=[]
iteration_count=[]
xi,yi,x_i,y_i=np.random.randint(low=0, high=99, size=4)
y_i%=50
yi%=50
a[xi,yi],a[x_i,y_i]=1,1
iteration=0
#print(a,xi,yi)
while len(a[a>0.999])!=4999:
  rand=np.random.randint(low=0, high=99, size=16)
  rand[1::2]%=50
  temp=[]
  for i in rand[::2]:
    for j in rand[1::2]:
      temp.append(a[i][j])
  #print(temp)
  k=7
  for i in rand[::2]:
    for j in rand[1::2]:
      a[i,j]=temp[k]
      k-=1
  for i in range(0,99):
    for j in range(0,49):
      if a[i,j]>0.999:
        a[i-1,j]+=0.25
        a[i+1,j]+=0.25
        a[i,j+1]+=0.25
        a[i,j-1]+=0.25
  b=a>0.999
  #print(a[b])
  num_ones=len(a[b])
  number_ones.append(num_ones)
  iteration_count.append(iteration)
  a[b]=1
  iteration+=1
  print(iteration, num_ones)
plt.plot(iteration_count, number_ones, 'r--')# red dashes
plt.axis([0, 60, 0, 6000])
plt.show()