# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:02:42 2018

@author: hp
"""
#FourCC character code:
#1. WMV2
#2. WMV1
#3. MJPG
#4. DIVX
#5. XVID
#6. H264



import cv2

def main():
    windowname="live video feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    
    # to save video in drive
    filename=r'C:\Users\hp\Downloads\forsk ml project\opencv program\result\output6.avi'
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution=(640,480)

    VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)

    
    
#    
#    if cap.isOpened():
#        ret,frame=cap.read()
#    else:
#        ret=False
        
    while True:
        ret,frame=cap.read()
        
        #it take video from webcam frame by frame and save or write it to given path
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowname,frame)
        if cv2.waitKey(1) ==27:
            break
    VideoFileOutput.release()
    cv2.destroyWindow(windowname)
    cap.release()
if __name__=="__main__":
    main()



0r




import cv2

cap=cv2.VideoCapture(0)

#to save webcam capture video in given path
filename=r'C:\Users\hp\Downloads\forsk ml project\opencv program\result\output4.avi'
#to save in XVID format
codec=cv2.VideoWriter_fourcc('X','V','I','D')
framerate=30
resolution=(640,480)

VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)

while True:
    ret,frame=cap.read()
    
    cv2.imshow('color',frame)
  
    VideoFileOutput.write(frame)
    
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




#to change color sffect



import cv2

cap=cv2.VideoCapture(0)

#to save webcam capture video in given path
filename=r'C:\Users\hp\Downloads\forsk ml project\opencv program\result\output4.avi'
#to save in XVID format
codec=cv2.VideoWriter_fourcc('X','V','I','D')
framerate=30
resolution=(640,480)

VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)

while True:
    ret,frame=cap.read()
    
    #to chane color effect to webcam video by giving cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB ....
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    cv2.imshow('color',frame)
  #to save or write frame by frame and save it to given path
    VideoFileOutput.write(frame)
    
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




0r



import cv2

def main():
    windowname="live video feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    
    # to save video in drive
    filename=r'C:\Users\hp\Downloads\forsk ml project\opencv program\result\output1.avi'
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution=(640,480)

    VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)

    
    
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        #it changes color effect to video webcam by taking 'cv2.COLOR_BGR2RGB' OR .BGR2GRAY  ....
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #it take video from webcam frame by frame and save or write it to given path
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowname,frame)
        if cv2.waitKey(1) ==27:
            break
    VideoFileOutput.release()
    cv2.destroyWindow(windowname)
    cap.release()
if __name__=="__main__":
    main()


