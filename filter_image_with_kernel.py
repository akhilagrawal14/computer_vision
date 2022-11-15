import cv2
import numpy as np







def get_filter(filter,custom_kernel=None):
    # sobel:gradient-based method that looks for strong changes in the 
    # first derivative of an image. mostly used for edge detection
    if filter=="sobel_right": #for x direction , right sobel
        sobel_right=np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])
        return sobel_right
    elif filter=="sobel_left": #for x direction , left sobel
        sobel_right=np.array([[1,0,-1],
                    [2,0,-2],
                    [1,0,-1]])
        return sobel_right
    elif filter=="sobel_bottom":  #for y direction, bottom sobel
        sobel_bottom=np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]])
        return sobel_bottom
    elif filter=="sobel_top":  #for y direction, top sobel
        sobel_top=np.array([[1,2,1],
                 [0,0,0],
                 [-1,-2,-1]])
        return sobel_top
    elif filter=="blur":
        blur=np.array([[0.0625,0.125,0.0625],
                       [0.125,0.25,0.125],
                       [0.0625,0.125,0.0625]])
        return blur
    elif filter=="emboss": 
        #This filter stamps and carves the active 
        # layer or selection, giving it relief with bumps 
        # and hollows. Bright areas are raised and dark 
        # ones are carved.
        emboss=np.array([[-2,-1,0],
            [-1,1,1],
            [0,1,2]])
    elif filter=="outline":
        # getting just the edges and else black 
        outline=np.array([[-1,-1,-1],
                         [-1,8,-1],
                         [-1,-1,-1]])
        return outline
    elif filter =="sharpen":  
        # sharpe edges in grayscale image
        sharpen=np.array([[0,-1,0],
                          [-1,5,-1],
                          [0,-1,0]])
        return sharpen
    elif filter=="custom":  
        #given filter already
        if custom_kernal is not None and type(custom_kernal) is np.ndarray:
            return custom_kernel
        elif custom_kernal is not None and type(custom_kernal) is list :
            return np.array(custom_kernel) #assuming size same not specifying 3*3 as can even increse it.
            

def filter_image(rgb_image,filter="sobel_right"):
    gray=cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)
    filter_matrix=get_filter(filter)
    filtered_image=cv2.filter2D(gray,-1,filter_matrix)
    return filtered_image