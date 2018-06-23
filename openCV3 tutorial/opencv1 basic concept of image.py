# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:37:16 2018

@author: hp
"""
#to show the version of opencv
import cv2
def main():
    print(cv2.__version__)
if __name__=="__main__":
    main()
    
#to show all funstion in cv2    
 dir(cv2)   


import cv2 
print(cv2.__version__)


import cv2 
def hello():
    #in window image read by two method
    #1. by "double salsh" or '\\'
    imgpath="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\lena_color_256.tif"
    #2. by giving 'r' in starting of path
    #imgpath=r"C:\Users\hp\Downloads\forsk ml project\opencv program\image\standard_test_images\lena_color_256.tif"
    img=cv2.imread(imgpath,0)
    
    cv2.imshow('lena',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    hello()



#to save image in specified path
import cv2

def main():
    
    imgpath="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\lena_color_256.tif"
    # 0: for gray scale
    #1 :for color image
    #-1 :for alpha transparency
    img=cv2.imread(imgpath,0)
    outpath="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\output\\lena_color_256.tif"
    cv2.imshow('lena',img)
    cv2.imwrite(outpath,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    hello()





#opencv concept of number ,images nad numpy
#Image =set of number
    

#for color images
color images is 3d image
<class 'numpy.ndarray'>
N dimensional array=composite data type
numpy=numerical python
unit8=unsigned integer 8 bits

for minimum 8 bits digit:
00000000 : min binary
0x00 :min  hexadecimal
0 :min decimal

for maximaum 8 bit digit:  
11111111 : max binary
0xFF : max hexa
255 : max decimal

0-255= 256 channels
#[125,137,226]=blue green red
#    125=blue
#    137=green
#    226=red
#    
generally channel arrage at RGB format
but comes to opencv it arranges at BGR format
img1.shape=(256,256,3)
where 
3: no of color channel BGR
256:height
256:width



import cv2 
def hello():
    imgpath="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\lena_color_256.tif"
    img1=cv2.imread(imgpath,1)
    
    #print(img1)
    
    print(type(img1))
    print(img1.dtype)
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    
if __name__=="__main__":
    hello() 



# for gray scale
gray scale represented by '0'
    
which is 2D image
it is gray image it has  no color
img1.shape=(256,256)
256=height
256=width

0-255=256
0=black  
255=white



import cv2 
def hello():
    imgpath="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\lena_color_256.tif"
    img1=cv2.imread(imgpath,0)
    
    print(img1)
    
    print(type(img1))
    print(img1.dtype)
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    
if __name__=="__main__":
    hello() 
