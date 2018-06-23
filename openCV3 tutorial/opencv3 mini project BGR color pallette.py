# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:24:00 2018

@author: hp
"""

import cv2
import numpy as np
def emptyFunction():
    pass
def main():
    #for color 3D images or windows
    img1=np.zeros((512,512,3),np.uint8)
    #opening window name
    windowName1='opencv BGR color palette'
    #create window scfreen
    cv2.namedWindow(windowName1)
     
    #create trackbar of BGR color range 0-255
    cv2.createTrackbar('B',windowName1,0,255,emptyFunction)
    cv2.createTrackbar('G',windowName1,0,255,emptyFunction)
    cv2.createTrackbar('R',windowName1,0,255,emptyFunction)
    
    #infinte loop for opening window until press ESC key
    while True:
         cv2.imshow(windowName1,img1)
          
         #27:ESC key press to quit
         if cv2.waitKey(1)==27:
             break
#for color changes screen
             #to show color changes effect in window
         blue=cv2.getTrackbarPos('B',windowName1)
         green=cv2.getTrackbarPos('G',windowName1)
         red=cv2.getTrackbarPos('R',windowName1)
         img1[:]=[blue,green,red]
         print(blue,green,red)
        
    cv2.destroyAllWindows()
    
    
if __name__=="__main__":
    main()
            