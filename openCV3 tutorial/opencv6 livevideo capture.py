# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:30:47 2018

@author: hp
"""

import cv2

def main():
    windowname="live video feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    
    
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        
        
        cv2.imshow(windowname,frame)
        if cv2.waitKey(1) ==27:
            break
    cv2.destroyWindow(windowname)
    cap.release()
if __name__=="__main__":
    main()
        

or



import cv2

def main():
    windowname="live video feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        
        output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        
        cv2.imshow("gray",output)
        cv2.imshow(windowname,frame)
        if cv2.waitKey(1) ==27:
            break
    cv2.destroyAllWindows()
    cap.release()
if __name__=="__main__":
    main()
        



or






import cv2

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('color',frame)
    cv2.imshow('title',gray)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()