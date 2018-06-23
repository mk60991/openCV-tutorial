# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:09:48 2018

@author: hp
"""

#to show images in both console and windows

import cv2
import matplotlib.pyplot as plt

def main():
    imgpath=r"C:\Users\hp\Downloads\forsk ml project\opencv program\image\standard_test_images\lena_color_256.tif"
    img=cv2.imread(imgpath,0)
    #to show images in console
    plt.imshow(img)
    plt.show()
    
    #to show image in outside window
    cv2.imshow('lena',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
    
if __name__=="__main__":
    main()
    




import cv2
import matplotlib.pyplot as plt


def main():
    imgpath=r"C:\Users\hp\Downloads\forsk ml project\opencv program\image\standard_test_images\lena_color_256.tif"
    img=cv2.imread(imgpath,0)
    #to show colored  images in console
    plt.imshow(img,cmap='Reds')
    plt.title("lena color images")
    plt.show()
    
    #to show default images in console
    plt.imshow(img)
    plt.title('default')
    plt.show()
    
    
    
if __name__=="__main__":
    main()
    
    
    
    
    
#to remove x axis scaling
#and y axis  scaling    
    
import cv2
import matplotlib.pyplot as plt

def hello():
    imgpath1=r"C:\Users\hp\Downloads\forsk ml project\opencv program\image\standard_test_images\lena_color_256.tif"

    img1=cv2.imread(imgpath1,0)
    plt.imshow(img1,cmap='gray')
    plt.title("lena images color")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img1)
    plt.title("default")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
if __name__=="__main__":
    hello()
    
    
    
when we read color image from path ,they didnot give that actual image from path path that actually exists
there is color conflict between RGB and BGR
opencv works on :BGR format
while matplotlib works on: RGB format
so to obtain color images from path that actaually axists in path
must com=nvert from BGR to RGB
    
  
import cv2
import matplotlib.pyplot as plt
def main():
    imgpath1=r"C:\Users\hp\Downloads\forsk ml project\opencv program\image\standard_test_images\lena_color_256.tif"
    img1=cv2.imread(imgpath1,1)
    
    #to remove color conflict must convert BGR to RGB
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    
    plt.imshow(img1)
    plt.title("actual color on path")
    plt.show()

    
if __name__=="__main__":
    main()
    
  
    
 # to show images in both RGB nad BGR   
import cv2
import matplotlib.pyplot as plt
def main():
    imgpath1=r"C:\Users\hp\Downloads\forsk ml project\opencv program\image\standard_test_images\lena_color_256.tif"
    img=cv2.imread(imgpath1,1)
    
    #to remove color conflict must convert BGR to RGB
    
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    #to show image in BGR
    plt.imshow(img)
    plt.title("BGR color")
    plt.show()
    
    #to show images in RGB
    plt.imshow(img1)
    plt.title("RGB color")
    plt.show()

    
if __name__=="__main__":
    main()
        
    
    
#to remove x axis scaling and y axis scaling
import cv2
import matplotlib.pyplot as plt
def main():
    imgpath1=r"C:\Users\hp\Downloads\forsk ml project\opencv program\image\standard_test_images\lena_color_256.tif"
    img=cv2.imread(imgpath1,1)
    
    #to remove color conflict must convert BGR to RGB
    
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    #to show image in BGR
    plt.imshow(img)
    plt.title("BGR color")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    #to show images in RGB
    plt.imshow(img1)
    plt.title("RGB color")
    plt.xticks([])
    plt.yticks([])
    plt.show()

    
if __name__=="__main__":
    main()
        
    
    
    
#small program to see various color conversion in opencv

import cv2
def main():
    j=0
    for filename in dir(cv2):
        if filename.startswith("COLOR_"):
            print(filename)
            j=j+1
            
    print("there are" +str((j+1)) + "color conversion flags in OpenCV.")

if __name__=="__main__":
    main()
           