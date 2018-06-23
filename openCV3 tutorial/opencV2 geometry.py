# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:26:34 2018

@author: hp
"""
import cv2
import numpy as np
 
def hello():
    
    img1=np.ones((512,512,3),np.uint8)
    print(img1)
    #cv2.line(img1,first coordinate,2nd coordinate,color,thickness)
    cv2.line(img1,(0,99),(99,0),(255,0,0),2)
    cv2.rectangle(img1,(100,60),(200,170),(0,255,0),2)
    cv2.circle(img1,(60,60),50,(0,0,255),-1)
    cv2.ellipse(img1,(160,260),(50,20),0,0,360,(127,127,127),-1)
    
    points=np.array([[80,2],[125,0],[179,0],[230,5],[30,50]],np.int32)
    points=points.reshape((-1,1,2))
    cv2.polylines(img1,[points],True,(0,255,255))
    
    text1="test text"
    cv2.putText(img1,text1,(150,150),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0))
    cv2.imshow('ish',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    hello()
    
    
    
    
