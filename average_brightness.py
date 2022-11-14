import cv2
import numpy as np


def average_brighness(rgb_image):
    """This function is useful in determining weather image is dark or not, day or night.
        because at dark image avg_brigness is les than 60 and 
        day it more than 130. Generally could have specific threshold as well"""
    hsv=cv2.cvtColor(rgb_image,cv2.COLOR_RGB2HSV)
    value_channel=hsv[:,:,2]
    sum_brightness=np.sum(value_channel)
    
    h,w=value_channel.shape
    area=h*w
    
    avg_brightness=sum_brightness/area
    
    return avg_brightness