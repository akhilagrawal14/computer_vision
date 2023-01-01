import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import math
import warnings
warnings.filterwarnings("ignore")



def threshold_image(img,threshold_type="otsu+blur",value=120,otsu_value=0):
    """
    simple thresholding: manually supply parameters, extremely well in controlled lighting conditions
    Otsu’s thresholding: more dynamic and automatically compute the optimal threshold
    adaptive thresholding: breaks the image down into smaller pieces, and thresholds each of these pieces separately and individually.
    
    cv.threshold(source, thresholdValue, maxVal, thresholdingTechnique) 
    """
    ret=0  #threshold value
    if threshold_type=="simple":
        ret,th_image = cv2.threshold(img, value, 255, cv2.THRESH_BINARY)
    elif threshold_type=="otsu":
        # Otsu's thresholding
        ret,th_image = cv2.threshold(img,otsu_value,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    elif threshold_type=="otsu+blur":
        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img,(5,5),0) #5*5 filter
        ret,th_image = cv2.threshold(blur,otsu_value,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    elif threshold_type=="adaptive":
        """cv2.adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)"""
        th_image = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,119,5)
    elif threshold_type=="adaptive+gaussian":
        th_image = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,119,5)
    
    return ret,th_image

if __name__ == "__main__":
    image_path=r"C:\Users\akhil\OneDrive\Pictures\cv_input_output\input_1.jpg"
    
    img=cv2.imread(image_path)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # returned_threshold,thresholded_image=threshold_image(img,threshold_type="simple",value=128)
    # print(f"simple threshold :{returned_threshold}")
    # filename = f'simple_threshold_Image_{returned_threshold}.jpg'
    # cv2.imwrite(filename, thresholded_image)
    
    # returned_threshold,thresholded_image=threshold_image(img,threshold_type="otsu",value=120)
    # print(f"otsu threshold :{returned_threshold}")
    # filename = f'otsu_threshold_Image_{returned_threshold}.jpg'
    # cv2.imwrite(filename, thresholded_image)

    # returned_threshold,thresholded_image=threshold_image(img,threshold_type="otsu+blur",value=120)
    # print(f"otsu plus blur threshold :{returned_threshold}")
    # filename = f'otsu_blur_threshold_Image_{returned_threshold}.jpg'
    # cv2.imwrite(filename, thresholded_image)
    
    returned_threshold,thresholded_image=threshold_image(img,threshold_type="adaptive")
    print(f"adaptive threshold :{returned_threshold}")
    filename = f'adaptive_threshold_Image.jpg'
    cv2.imwrite(filename, thresholded_image)
    
    returned_threshold,thresholded_image=threshold_image(img,threshold_type="adaptive+gaussian")
    print(f"adaptive+gaussian threshold :{returned_threshold}")
    filename = f'adaptive_gaussian_threshold_Image.jpg'
    cv2.imwrite(filename, thresholded_image)