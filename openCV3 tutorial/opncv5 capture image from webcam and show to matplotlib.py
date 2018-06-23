# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:22:42 2018

@author: hp
"""


#to capture image from webcam nad show in actual color RGB

import cv2
import matplotlib.pyplot as plt

def main():
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret=False
        
    img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    plt.imshow(img1)
    plt.title('color image RGB')
    plt.show()
    
    cap.release()
    
if __name__=="__main__":
    main()
        





import cv2
import matplotlib.pyplot as plt

def main():
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret=False
        
    img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    plt.imshow(img1)
    plt.title('color image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    cap.release()
    
if __name__=="__main__":
    main()