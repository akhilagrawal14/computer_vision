import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import math
import warnings
warnings.filterwarnings("ignore")


def flip_image(img,along="x"):
    if along == "x":
        flipped_img = cv2.flip(img, 0)  # 0 for  x-axis
    elif along == "y":
        flipped_img = cv2.flip(img, 1)  # 1 for  y-axis
    elif along == "xy":
        flipped_img= cv2.flip(img, -1)  # -1 for  a-axis and y-axis
    else:
        print("no valid axis given, returning black image")
        flipped_img = np.zeros(img.shape,dtype=np.uint8)

    return flipped_img

def rotate_image(img,angleInDegrees=0):
    # angle +ve for clockwise and -ve for anticlockwise
    
    #angleInDegrees=int(-1*angleInDegrees)
    # rotate at angle for a given image
    h, w = img.shape[:2]
    #height , width, channel
    image_center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(image_center,angleInDegrees,1)  #center, angle ,scale

    rad = math.radians(angleInDegrees)
    b_w = int((h * abs(math.sin(rad))) + (w * abs(math.cos(rad))))
    b_h = int((h * abs(math.cos(rad))) + (w * abs(math.sin(rad))))

    M[0, 2] += ((b_w / 2) - image_center[0])
    M[1, 2] += ((b_h / 2) - image_center[1])

    rotated_image = cv2.warpAffine(img,M,(b_w, b_h), flags=cv2.INTER_LINEAR)

    return rotated_image

def write_text(img,text,position="blc",txt_color=(36, 255, 12),thickness=2):
    """txt_color in rgb , """
    h,w,c=img.shape # h,w,c
    # tuple needed in width, height or x,y format
    if position=="trc":
        poc= (0+int(w/10),0+int(h/10)) #top right corner 
    elif position=="tlc":
        poc= (w-int(w/8),0+int(h/10)) #top left corner 
    elif position=="brc":
        poc= (0+int(w/10),h-int(h/10)) #bottom right corner 
    elif position=="blc": 
        poc= (w-int(w/8),h-int(h/10)) #bottom left corner 
    else:
        print("no valid position given among trc(top right corner),tlc,brc,blc(bottom left corner). Returning black image")
        return_img = np.zeros(img.shape,dtype=np.uint8)
        return return_img

    # write text given rectangle bbox cordinate
    #cv2.putText(image, 'Fedex', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    txt_image=cv2.putText(img.copy(), text, poc, cv2.FONT_HERSHEY_SIMPLEX, 4, txt_color, thickness, cv2.LINE_AA)
    '''
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness)
    img – It is the image on which the text has to be written.
    text – It is the text that needs to be put on the image
    org – Bottom-left corner of the text string in the image.
    fontFace – The font of the text. See the font types available in OpenCV here.
    fontScale – This value scales the size of the text by multiplying its base size.
    color – The color of the text.
    thickness – The thickness of the line of text
    '''
    return txt_image

def draw_rectangle(img,start,end,color=(36,255,12),thickness=2):
    #start in x,y format
    #end  represents the bottom right corner of rectangle
    #color for green is (36,155,12)

    rec_image = cv2.rectangle(img.copy(), start, end, color, thickness)
    
    return rec_image

def rectangle_with_text(img,start,end,text,color=(36,255,12),thickness=2):
    h,w,c=img.shape
    txt_coordinate=(start[0],start[1]-20)
    if txt_coordinate[1]<0:
        txt_coordinate=(start[0],0+int(h/10))
    print(txt_coordinate)

    rec_image = cv2.rectangle(img.copy(), start, end, color, thickness)
    txt_image=cv2.putText(rec_image, text, txt_coordinate, cv2.FONT_HERSHEY_SIMPLEX, 4, color, thickness, cv2.LINE_AA)

    return txt_image


if __name__ == "__main__":
    image_path=r"C:\Users\akhil\OneDrive\Pictures\nice images\wp3156016.jpg"
    
    img=cv2.imread(image_path)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    fliped_image=flip_image(img,along="xy")
    fliped_image=cv2.cvtColor(fliped_image, cv2.COLOR_RGB2BGR)
    filename = 'Flipped_Image.jpg'
    cv2.imwrite(filename, fliped_image)
    
    rotated_45_clockwise=rotate_image(img,angleInDegrees=45)
    rotated_45_clockwise=cv2.cvtColor(rotated_45_clockwise, cv2.COLOR_RGB2BGR)
    filename = 'rotated_Image.jpg'
    cv2.imwrite(filename, rotated_45_clockwise)
    
    txt_image=write_text(img,"dragon",position="blc")
    txt_image=cv2.cvtColor(txt_image, cv2.COLOR_RGB2BGR)
    filename = 'txt_Image.jpg'
    cv2.imwrite(filename, txt_image)
    
    rec_image=draw_rectangle(img,(1830,230),(3150,1900))
    rec_image=cv2.cvtColor(rec_image, cv2.COLOR_RGB2BGR)
    filename = 'rectangle_Image.jpg'
    cv2.imwrite(filename, rec_image)
    
    rec_txt_image=rectangle_with_text(img,(1830,230),(3150,1900),"Dragon GOT",thickness=7)
    rec_txt_image=cv2.cvtColor(rec_txt_image, cv2.COLOR_RGB2BGR)
    filename = 'rec_with+text_Image.jpg'
    cv2.imwrite(filename, rec_txt_image)
    
    
    
    
    
    
    

