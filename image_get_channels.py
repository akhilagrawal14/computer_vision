import cv2
import numpy as np


""" here all image inputs will be of numpy  RGB and outputs the required image array""" 

#utils 
def get_rgb_channel(img):
    r,g,b=img[:,:,0],img[:,:,1],img[:,:,2]
    return r,g,b

def get_red_channel(img):
    r=img[:,:,0]
    return r

def get_green_channel(img):
    g=img[:,:,1]
    return g

def get_blue_channel(img):
    b=img[:,:,2]
    return b

def get_hsv_channel(img):
    #hue,value,saturation for color,brighness,greyness
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h,s,v=img_hsv[:,:,0],img_hsv[:,:,1],img_hsv[:,:,2] 
    return h,s,v

def get_hue_channel(img):
    #hue,value,saturation for color,brighness,greyness
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h=img_hsv[:,:,0] 
    return h

def get_saturation_channel(img):
    #hue,value,saturation for color,brighness,greyness
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    s=img_hsv[:,:,1] 
    return s

def get_value_channel(img):
    #hue,value,saturation for color,brighness,greyness
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    v=img_hsv[:,:,2] 
    return v

def get_cymk_channel(img):
    #CYAN, MAGENTA, YELLOW , and BLACK
    img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    bgr = img.astype(float)/255

    # Extract channels
    with np.errstate(invalid='ignore', divide='ignore'):
        K = 1 - np.max(bgr, axis=2)
        C = (1-bgr[...,2] - K)/(1-K)
        M = (1-bgr[...,1] - K)/(1-K)
        Y = (1-bgr[...,0] - K)/(1-K)

    # Convert the input BGR image to CMYK colorspace
    CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)

    # Split CMYK channels
    Y, M, C, K = cv2.split(CMYK)
    
    return C,Y,M,K

