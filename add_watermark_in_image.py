import cv2
import numpy as np
"""adding logo"""

#here currently removing original image part completely rather than having some part still.
def add_image_watermark(image,watermark_image,percentage_watermark=0.2):
    
    # take h,w percentage as background image for forground image resize
    # resize forground image
    img_shape=image.shape
    watermark_shape=watermark_image.shape
    ratio_watermarked=watermark_shape[0]/watermark_shape[1] # height/width
    print(img_shape,watermark_shape)
    
    new_width=int(img_shape[0] * percentage_watermark)
    new_height=int(new_width *ratio_watermarked) 
    new_dim = (new_width,new_height)
    watermarked_resized_img = cv2.resize(watermark_image, new_dim, interpolation=cv2.INTER_AREA)
    # take position for foreground, default bottom_right
    print(new_dim)
    #add transperency if given , default none
    top_y=img_shape[0]-new_dim[1]  # total height - height of watermark
    bottom_y=img_shape[0]
    left_x=img_shape[1]-new_dim[0]
    right_x=img_shape[1]
    print(top_y,bottom_y, left_x,right_x)
    roi = image[top_y:bottom_y, left_x:right_x]
    # g(x)=α.src1 + ß.src2 + γ ,  cv.addWeighted(src1, alpha, src2, beta, gamma)
    result = cv2.addWeighted(roi, 0, watermarked_resized_img, 1, 0)
    image[top_y:bottom_y, left_x:right_x] = result
    
    #return new image generated
    
    return image


if __name__ == "__main__":
    image=cv2.imread(r"C:\Users\akhil\OneDrive\Pictures\nice images\IMG_20221008_121556.jpg")
    watermarked_img=cv2.imread(r"C:\Users\akhil\OneDrive\Pictures\me\vaccine_qr_code_akhil.jpg")
    
    result_image=add_image_watermark(image,watermarked_img,percentage_watermark=0.1)
    
    filename = 'Watermakared_Image.jpg'
    cv2.imwrite(filename, result_image)