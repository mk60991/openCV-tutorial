# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:14:24 2018

@author: hp
"""


import cv2
import matplotlib.pyplot as plt


def emptyfunction():
    pass

def main():
    path="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\"
    
    imgpath2=path +"peppers_color.tif"
    imgpath1=path +"mandril_color.tif"

    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
 
    

    
    #add two images by weight and give blending effect to image
    output=cv2.addWeighted(img1,0.5,img2,0.5,0)
    windowName="Transition Demo"
    cv2.namedWindow(windowName)
    # it only create trackbar on window but doesnot give blending effect
    cv2.createTrackbar('Alpha',windowName,0,100,emptyfunction)

    while True:
        cv2.imshow(windowName,output)
        if cv2.waitKey(1)==27:
            break
        # blending effect provide by this 'trackbarpos'
        alpha=cv2.getTrackbarPos('Alpha',windowName)/100
        beta=1-alpha
        
        #finally give blending effect to two images
        output=cv2.addWeighted(img1,alpha,img2,beta,0)
        print(alpha,beta)
        
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()    
    