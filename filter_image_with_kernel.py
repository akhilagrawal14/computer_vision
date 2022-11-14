import cv2
import numpy as np







def get_filter(filter):
    # sobel:gradient-based method that looks for strong changes in the 
    # first derivative of an image. mostly used for edge detection
    if filter=="sobel_x": #for x direction
        sobel_x=np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])
        return sobel_x
    elif filter=="sobel_y":  #for y direction
        sobel_y=np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]])
        return sobel_y

def filter_image(rgb_image,filter="sobel_x"):
    gray=cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)
    filter_matrix=get_filter(filter)
    filtered_image=cv2.filter2D(gray,-1,filter_matrix)
    return filtered_image