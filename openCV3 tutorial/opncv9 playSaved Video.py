# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:43:30 2018

@author: hp
"""


#to play video from saved video
import cv2

def main():
    windowname="live video feed"
    cv2.namedWindow(windowname)
   
     
    filename=r'C:\Users\hp\Downloads\forsk ml project\opencv program\result\output6.avi'
    #taken video from saved video in drive
    cap=cv2.VideoCapture(filename)

    #looping is true until video play    
    while (cap.isOpened()):
        ret,frame=cap.read()
        print(ret)
        

        #if ret is true it read the video
        #if ret is false it destroy the video
        if ret:
            cv2.imshow(windowname,frame)
            if cv2.waitKey(1) ==27:
                break
        else:
            break

  
    cv2.destroyWindow(windowname)
    cap.release()
if __name__=="__main__":
    main()




0r


import cv2

#to save webcam capture video in given path
filename=r'C:\Users\hp\Downloads\forsk ml project\opencv program\result\output4.avi'
#to read video from filepath not from webcam
cap=cv2.VideoCapture(filename)

#it read video until play
while True:
    ret,frame=cap.read()
    
    #if video is about to end on playing it return false
    #automatically quit video
    if ret:
         cv2.imshow('color',frame)
         if cv2.waitKey(1) & 0XFF==ord('q'):
             break
    else:
        break

   
cap.release()
cv2.destroyAllWindows()





above vdeo playback speed is very high due to 
when video is capturing from wehave given framerate=30
30 fps=videocapture rate

it will solved by giving appropriate argument in 'waitKey()'
30 FPS
1000 millisecond = 1 second
30 millisecond
1000/video capture rate
1000/30=33
if waitKey(33)it give smooth palyback speed
if argument of waitKey is increased or greater than value 33 it playback speed get slower:
if argument of waitKey is decreased or lower than value 33 it playback speed get higher:   
waitKey argument value 1 give fastest video playback    
    
import cv2

#to save webcam capture video in given path
filename=r'C:\Users\hp\Downloads\forsk ml project\opencv program\result\output4.avi'
#to read video from filepath not from webcam
cap=cv2.VideoCapture(filename)

#it read video until play
while True:
    ret,frame=cap.read()
    
    #if video is about to end on playing it return false
    #automatically quit video
    if ret:
         cv2.imshow('color',frame)
         #33 give smooth playback
         #if cv2.waitKey(33) & 0XFF==ord('q'):
         
         #120 give slower video playback
         #if cv2.waitKey(120) & 0XFF==ord('q'):
         #lower argument give faster video playback if value lower than 33
         if cv2.waitKey(5) & 0XFF==ord('q'):
             break
    else:
        break

   
cap.release()
cv2.destroyAllWindows()
