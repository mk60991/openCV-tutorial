# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:40:45 2018

@author: hp
"""

import cv2
import matplotlib.pyplot as plt

def main():
    path="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\"
    
    imgpath2=path +"peppers_color.tif"
    imgpath1=path +"mandril_color.tif"

    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
 
   
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    
    alpha=0.5
    beta=0.5
    gamma=0
    
    #add two images by weight and give blending image
    output=cv2.addWeighted(img1,alpha,img2,beta,gamma)
    

    titles=['monkey','fruits','addweighted']
    images=[img1,img2,output]
    for i in range(3):
          plt.subplot(1,3,i+1)
          plt.imshow(images[i])
          plt.title(titles[i])
        
  
    
    plt.show()
    
    
if __name__=="__main__":
    main()    
    
    





import cv2
import numpy as np
import time

import matplotlib.pyplot as plt

def main():
    path="C:\\Users\\hp\\Downloads\\forsk ml project\\opencv program\\image\\standard_test_images\\"
    
    imgpath2=path +"peppers_color.tif"
    imgpath1=path +"mandril_color.tif"

    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)

#    
#    #if we increase the interval recommended to decrease the delay time
    # np.linspace(start,end,interval)
    # eg. (0,1,5)=[0.,0.25,0.5,0.75,1. ]
    for i in np.linspace(0,1,100):
        alpha=i
        beta=1-alpha
        output=cv2.addWeighted(img1,alpha,img2,beta,0)
        cv2.imshow('Transition',output)
        #delay time in second
        time.sleep(0.05)
        if cv2.waitKey(1)==27:
            break
    
#
    cv2.destroyAllWindows()
    
    
if __name__=="__main__":
    main()    
    
    
    
    
import numpy as np
np.linspace(0,1,5)