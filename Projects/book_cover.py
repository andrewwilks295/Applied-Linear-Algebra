# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:46:52 2023

@author: wilks
"""

# requesting the image from github
def get_image(url):
  import io
  import requests as re
  from PIL import Image

  get = re.get(url) # fetch the image
  img_bytes = io.BytesIO(get.content) # create propper binary object
  img = Image.open(img_bytes) # parse image to an image object

  return img
#%%
import matplotlib.pyplot as plt
import numpy as np

url = r'https://raw.githubusercontent.com/emisseldine/OpenLinear/main/Chapter6/images/bookcover.png'
cover = np.asarray(get_image(url))[:,:,0]
color = 'Blues_r' 

# processing image
plt.figure(figsize=(9,6))
plt.imshow(cover,cmap=color)
plt.axis('off')
plt.show()

#%% Task 1
U,sigma,VT = np.linalg.svd(cover)
#compute the SVD of cover where cover = U @ Sigma @ V.T

#%% Task 2
reduced_svd = lambda U , sigma ,VT , k : U [: ,: k] @ np . diag ( sigma [: k ]) @ VT [:k ,:]
num_vals = [1,2,3,4,5,10,25,100,200,300,400,500,1000,1500,2000]
for k in num_vals:
    blur = reduced_svd(U, sigma, VT, k)#compute the rank-k singular reduction of blur
    plt.figure(figsize=(9,6))
    plt.imshow(blur,cmap=color)
    plt.title(f"k = {k}")
    plt.axis('off')
    plt.show()
#Analyze the quality of an image compared to data savings
print("The higher the value, the closer it is to the origional.")
print("K isn't the number of pixles but if you compare k = 1 and")
print("k = 25, you already have a majority of your picture.")
print("Looking at k = 200, I think this is the most reduction you")
print("can get away with.")

#%% Task 3
k = 1242#the rank at which the singular reduction obtains 90% of the original image's size

blur = reduced_svd(U, sigma, VT, k) #compute the rank-k singular reduction of blur
plt.figure(figsize=(9,6))
plt.imshow(blur,cmap=color)
plt.title(f"k = {k}")
plt.axis('off')
plt.show()