import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
import io
from PIL import Image

def get_color_distribution(img):
    """Takes RGB image"""
    hsv_image=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    color_dict_HSV = {
    'black': [[180, 255, 30], [0, 0, 0]],
    'white': [[180, 18, 255], [0, 0, 231]],
    'red1': [[180, 255, 255], [159, 50, 70]],
    'red2': [[9, 255, 255], [0, 50, 70]],
    'green': [[89, 255, 255], [36, 50, 70]],
    'blue': [[128, 255, 255], [90, 50, 70]],
    'yellow': [[35, 255, 255], [25, 50, 70]],
    'purple': [[158, 255, 255], [129, 50, 70]],
    'orange': [[24, 255, 255], [10, 50, 70]],
    'gray': [[180, 18, 230], [0, 0, 40]],
    'pink' :[[180, 255, 255], [160, 0, 0]]
        }
    
    result={}

    fig, ax = plt.subplots(math.ceil(len(color_dict_HSV)/3), 3, figsize = (8,8), dpi = 160)

    
    i=0
    j=0
    for key,value in color_dict_HSV.items():
        upper=np.array(value[0])
        lower=np.array(value[1])
        mask=cv2.inRange(hsv_image,lower,upper)
        count=np.count_nonzero(mask)
        total=mask.flatten().shape[0]
        result[key]=count/total
        ax[i,j].imshow(mask,cmap="gray")  
        ax[i,j].set_title(key)
        ax[i,j].axis('off')
        j+=1
        if j%3==0:
            j=0
            i+=1
    result['red']=result['red1']+result['red2']
    if 'red1' in result:
        del result['red1']
    if 'red2' in result:
        del result['red2']    
    print(result)

    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_masked = Image.open(img_buf)
    
    plt.clf()
    plt.figure(figsize=(10, 5))
    plt.bar(*zip(*result.items()),width=0.5,align='center')
    plt.xlabel("color")
    plt.ylabel(" %  color/100")
    plt.title("image color distribution")
    
    img_buf2 = io.BytesIO()
    plt.savefig(img_buf2, format='png')
    img_distribution_bar = Image.open(img_buf2)
    
    return result,img_masked,img_distribution_bar
    

if __name__ == '__main__':
    img_path=r"C:\Users\akhil\OneDrive\Pictures\nice images\IMG_20221008_121556.jpg"
    img = cv2.imread(img_path)
    result,img_masked,img_distribution_bar=get_color_distribution(img)
    
    filename = 'color_distribution_of_image.png'
    img_masked.save(filename)
    
    filename2 = 'color_distribution_bar_graph.png'
    img_distribution_bar.save(filename2)