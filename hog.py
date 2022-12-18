#importing required libraries
from skimage.io import imread
from skimage.io import imsave
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import numpy as np
from skimage import img_as_ubyte


"""
Here image is in skimage format from from skimage.io import imread
# reading the image
img = imread(r"input_1.jpg")
"""

def resize_image(img,fixed_resized_height):
    ratio=img.shape[1]/img.shape[0]  #width/height
    resized_shape=(fixed_resized_height,int(ratio*fixed_resized_height),3)
    resized_img = resize(img, resized_shape)
    return resized_img

def image_to_hog(img,orientations=9, pixels_per_cell=(16, 16),cells_per_block=(2, 2),fixed_resized_height=256):
    img=resize_image(img,fixed_resized_height)
    fd, hog_image = hog(img, orientations=orientations, pixels_per_cell=pixels_per_cell,
                    cells_per_block=cells_per_block, visualize=True, multichannel=True,
                    feature_vector = False)
    # feature vector format 
    # # row block , column block , row cell , column cell , orientation
    print(f"feature vector shape: {fd.shape}")
    return fd, hog_image


if __name__ == '__main__':
    img_path=r"C:\Users\akhil\OneDrive\Pictures\Saved pictures\k0Q9ME.jpg"
    img = imread(img_path)
    fd, hog_image=image_to_hog(img,orientations=16,fixed_resized_height=512)
    
    filename = 'hog_Image.jpg'
    imsave(filename,img_as_ubyte(hog_image))