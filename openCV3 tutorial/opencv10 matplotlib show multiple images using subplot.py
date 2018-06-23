# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 12:06:09 2018

@author: hp
"""



#to show multiple images in console
import cv2
import matplotlib.pyplot as plt

def main():
    path="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\"
    
    imgpath2=path +"peppers_color.tif"
    imgpath1=path +"mandril_color.tif"
   
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
   
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    #to show images in console
    plt.imshow(img1)
    plt.title("monkey")
    plt.show()
    
    plt.imshow(img2)
    plt.title("fruits")
    plt.show()
    
    
if __name__=="__main__":
    main()
    
    
    
 
    #by using 'subplot' function to show multiple images
    
# plt.subplot(no of rows,no of columns,position of images)   
    
    
import cv2
import matplotlib.pyplot as plt

def main():
    path="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\"
    
    imgpath2=path +"peppers_color.tif"
    imgpath1=path +"mandril_color.tif"
    imgpath3=path +"woman_blonde.tif"
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    img3=cv2.imread(imgpath3,1)
   
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    img3=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
   
    
    #to show images in console
    plt.subplot(1,3,1)
    plt.imshow(img1)
    plt.title("monkey")
    
    plt.subplot(1,3,2)
    plt.imshow(img2)
    plt.title("fruits")
    
    plt.subplot(1,3,3)
    plt.imshow(img3)
    plt.title("girls")
    
    plt.show()
    
    
if __name__=="__main__":
    main()    




#by using 'for loop'

import cv2
import matplotlib.pyplot as plt

def main():
    path="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\"
    
    imgpath2=path +"peppers_color.tif"
    imgpath1=path +"mandril_color.tif"
    imgpath3=path +"woman_blonde.tif"
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    img3=cv2.imread(imgpath3,1)
   
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    img3=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
   
    titles=['monkey','fruits','girls']
    images=[img1,img2,img3]
    for i in range(3):
          plt.subplot(1,3,i+1)
          plt.imshow(images[i])
          plt.title(titles[i])
        
  
    
    plt.show()
    
    
if __name__=="__main__":
    main()    
