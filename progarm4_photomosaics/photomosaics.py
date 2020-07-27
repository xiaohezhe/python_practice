import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load an color image in grayscale

img_colorful = cv2.imread('pineapple.jpg',1)
img_original = cv2.imread('pineapple.jpg',1)

# (467, 700, 3) tuple of number of rows, columns and channels (if image is color)
img_shape = img_colorful.shape
print(img_shape) 
print(img_colorful.size)

shrink_imge = cv2.resize(img_colorful,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
height,width=img_colorful.shape[:2]#取shape列表里的两个值

print(height,width)


M=cv2.getRotationMatrix2D((width/2,height/2),180,1)
dst=cv2.warpAffine(img_colorful,M,(width,height))#warpAffine 映射函数

#directly changing in the input image 'img_colorful'
rectangle = cv2.rectangle(img_colorful,(300,200),(400,300),(0,0,255),-1)#blue,green,red,-1是决定粗细的参数

#边缘检测滤镜
edges = cv2.Canny(img_original,100,300)

#高斯模糊滤镜
filter_GaussianBlur = cv2.GaussianBlur(img_original,(5,5),0)


#复古滤镜
# 创建高斯滤波器
kernel_x = cv2.getGaussianKernel(width,200)
kernel_y = cv2.getGaussianKernel(height,200)
kernel = kernel_y * kernel_x.T
filter = 255 * kernel / np.linalg.norm(kernel)
vintage_im = np.copy(img_original)

for i in range(3):
    vintage_im[:,:,i] = vintage_im[:,:,i] * filter

while(1):
    cv2.imshow('img_shrink_window',shrink_imge)
    cv2.imshow('img_origianl',img_original)
    cv2.imshow('img',img_colorful)
    cv2.imshow('img_rotate',dst)
    cv2.imshow('img_filter_canny',edges)
    cv2.imshow('img_filter_gauss',filter_GaussianBlur)
    cv2.imshow('img_filter_oldversion',vintage_im)
    if cv2.waitKey(0):
        break
cv2.destroyAllWindows()   
