# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:59:05 2018

@author: hp
"""


#arithmetic operation on images
#addition
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
    
    
    #aruthmatic operation on images
    add=img1+img2
    sub=img1-img2
    sub2=img2-img1
   
    titles=['monkey','fruits','add','sub','sub2']
    images=[img1,img2,add,sub,sub2]
    for i in range(5):
          plt.subplot(1,5,i+1)
          plt.imshow(images[i])
          plt.title(titles[i])
        
  
    
    plt.show()
    
    
if __name__=="__main__":
    main()    
    
    
    
    
    
    
#arithmetic operation with numbers
    
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
    
    
    #aruthmatic operation on images "with any integer numbers"
    add=img1+50
    sub=img1-50
    sub2=50-img1
   
    titles=['monkey','fruits','add','sub','sub2']
    images=[img1,img2,add,sub,sub2]
    for i in range(5):
          plt.subplot(1,5,i+1)
          plt.imshow(images[i])
          plt.title(titles[i])
        
  
    
    plt.show()
    
    
if __name__=="__main__":
    main()    
    
    
    
    
#arithmetic operation on images 
    #multiplication and division
    
    
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
    
    
    #aruthmatic operation on images
    mul=img1*img2
    div=img1/img2
    
   
    titles=['monkey','fruits','mul','div']
    images=[img1,img2,mul,div]
    for i in range(4):
          plt.subplot(1,4,i+1)
          plt.imshow(images[i])
          plt.title(titles[i])
        
  
    
    plt.show()
    
    
if __name__=="__main__":
    main()    
    
    
    
    
#arithmetic operation on images with integer or real numbers
    
    #multiplication or division
    
    
    
    
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
    
    
    #aruthmatic operation on images with integer or real numbers
    mul=img1*60
    div=img1/60
    mul1=img2*5.3
    div1=img2/2.8
   
    titles=['monkey','fruits','mul','div','mul1','div1']
    images=[img1,img2,mul,div,mul1,div1]
    for i in range(6):
          plt.subplot(1,6,i+1)
          plt.imshow(images[i])
          plt.title(titles[i])
        
  
    
    plt.show()
    
    
if __name__=="__main__":
    main()    
    