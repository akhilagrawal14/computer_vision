import cv2
import numpy as np
import os

import utils

def get_image_info(image):
    """INPUT:
        image: cv2 image
        OUTPUT:
        dict containing info
    """
    image_size=image.shape
    #print(image_size)
    size=len(image_size)
  
    print(f"new size {size} , image_size: {image_size}")
    info={}
    image_type={2:"GRAYSCALE",3:"COLOR",4:"RGBA"}
    info['height']=image_size[0]
    info['width']=image_size[1]
    
    if size>2 :
        info['channel']=image_size[2]
    if size>3:
        info['transperancy']=image_size[3]
    info['type']=image_type[size]
    return info
    
def isgray(imgpath):
    img = cv2.imread(imgpath)
    if len(img.shape) < 3: return True
    if img.shape[2]  == 1: return True
    b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
    if (b==g).all() and (b==r).all(): return True
    print("given image is not a grayscale image")
    return False

def read_image_from_path(image_path,required_format="RGB"):
    
    print(f"given image path : ->{image_path}")
    
    if isgray(image_path):
        required_format="GRAYSCALE"
    
    if required_format == "RGB":
        img = cv2.imread(image_path,cv2.IMREAD_COLOR) #no transparency channel
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif required_format == "BGR":
        img = cv2.imread(image_path,cv2.IMREAD_COLOR) #no transparency channel
    elif required_format == "GRAYSCALE":
        img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    elif required_format == "UNCHANGE":
        img = cv2.imread(image_path,cv2.IMREAD_UNCHANGED) #good if transperency or alpha
    else:
        img=np.zeros((256,256,3), np.uint8) #no image so giving black image
    
    return img

def image_write(image,file_name,current_format="RGB",extension=".jpeg",path_to_save="./images"):
    full_path=os.path.join(path_to_save,file_name+extension)
    utils.create_dir(path_to_save)
    try:
        if current_format=="RGB":
            image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        response=cv2.imwrite(full_path,image)
    except Exception as e:
        print(f"Error occured while writing into {path_to_save}: {e}")
    return response

if __name__ == "__main__":
    
    image_path=r"C:\Users\akhil\OneDrive\Pictures\me\IMG_20221010_112517.jpg"
    
    image_rgb=read_image_from_path(image_path,required_format="RGB")
    print(f"Is image grayscale: {isgray(image_path)}")
    info_rgb=get_image_info(image_rgb)
    print(f"image info:{info_rgb}")
    
    
    image_path2=r"C:\Users\akhil\OneDrive\Pictures\me\vaccine_qr_code_akhil.jpg"
    image_grey=read_image_from_path(image_path2,required_format="RGB")
    print(f"Is image grayscale: {isgray(image_path2)}")
    info_rgb2=get_image_info(image_grey)
    print(f"image info:{info_rgb2}")
    