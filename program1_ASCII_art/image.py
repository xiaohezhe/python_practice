from PIL import Image
import numpy as np
#####################################################################
####Load your image’s pixel data into a 2-dimensional array ########                       
'''
#open image
im = Image.open("pineapple.jpg")

#check the image contents
print(im.format, im.size, im.mode)##size-tuple(width,height)

#display the image
im.show()


#Image类返回矩阵的操作
data = list(im.getdata())
print(data)

data_2_dimensional = np.array(im)

print(data_2_dimensional)

wide = (data_2_dimensional).shape
print(wide)
for x in range(wide[0]):
    for y in range(wide[1]):
        print((data_2_dimensional[x,y]))
raise ValueError() ## display every position(x,y) color(Red, Green, Blue)


# print(data)
# print(np.array(data))
# print(np.array(data).shape)
# ex_tuple = (1,2,3)
# ex_list = [1,2,3]
# print(np.array(ex_tuple)-np.array(ex_list))
# print(np.array(data).flatten())

# =============================================================================
# data_array=np.array(data).reshape((700,467,3))
# print(data_array)
# 
# a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# 
# print(list(a))
# print(np.array(a))
# #data_array=np.array(a).reshape((2,2,3))
# 
# print(data_array[100,100])
# =============================================================================
'''

#####################################################################
####Convert the RGB tuples into single brightness numbers ########  

#open image
im = Image.open("pineapple.jpg")

im.show()

data = list(im.getdata())#list all the tuples of grids
data_2_dimensional = np.array(im)

wide = (data_2_dimensional).shape
print(wide)  #(467, 700, 3)


number_light = []
for x in range(wide[0]):
    for y in range(wide[1]):
        R = data_2_dimensional[x,y][0]
        G = data_2_dimensional[x,y][1]
        B = data_2_dimensional[x,y][2]
        average = int((R + G + B) / 3)
        number_light.append(average)
       
print(number_light) #number_light is the array of single brightness values 
        

#####################################################################
####Convert brightness numbers to ASCII characterss #######    


lightness = ("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
print(len(lightness))#total 65 characters, 2 '\' can ouput the later character
print(lightness)



#repeat ecah character 4 times 
#append() 方法用于在列表末尾添加新的对象。

l=[]
for elem in lightness:
    for i in range(4): #dont need define i in advance
        l.append(elem)
print(l)
print(len(l))
print(l.index("v"))#v is the index[128]
print(l[252])#indexp[252] is @
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
def calculation_brightness_to_character(number):
    index_lightness = 0
    if number <=254:
        index_lightness = number
    else:
        index_lightness = 256
    return index_lightness 

new_array = []      
        
for mem in number_light:
    new_array.append(calculation_brightness_to_character(mem))
print(new_array)     
        
        
    





    
    





















