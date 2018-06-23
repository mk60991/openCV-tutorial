# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:30:00 2018

@author: hp
"""

import cv2

def main():
    windowname="live video feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    
    
    #if resolution is higher then frame rate is lower
    #if resolution is lower then frame rate is higher
    #for webcam resolution
    print("width :" +str(cap.get(3)))
    print("height :" +str(cap.get(4)))
    
    #my webcam max resolution by setting itself
    cap.set(3,1280)
    cap.set(4,720)
    print("width :" +str(cap.get(3)))
    print("height :" +str(cap.get(4)))
    
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
        
    
    

import cv2

cap=cv2.VideoCapture(0)

#resolution of webcam
print("width :" +str(cap.get(3)))
print("height :" +str(cap.get(4)))

#to set webcam resolution manually
#if webcam resolution high ,frame rate will be lower
#f webcam resolution low ,then frame rate will be higher
cap.set(3,1280)
cap.set(4,720)
print("width :" +str(cap.get(3)))
print("height :" +str(cap.get(4)))
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('color',frame)
    cv2.imshow('title',gray)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()