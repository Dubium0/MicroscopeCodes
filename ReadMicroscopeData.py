# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:53:14 2022

@author: LENOPC
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(2)


while cap.isOpened():
    ret,frame = cap.read()
    
    cv2.imshow("microscope",frame)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    

