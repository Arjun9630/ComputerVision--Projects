import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]]) # Converts to a NumPy array representing a single pixel in BGR

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) #Coverts to HSV colorspace { hsvC = [[[ 30 255 255]]] for yellow in BGR}
    lowerLimit = hsvC[0][0][0] -  10, 100, 100 #setting the range
    upperLimit = hsvC[0][0][0] +  10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8) #converts to np array i.e. opencv format
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
