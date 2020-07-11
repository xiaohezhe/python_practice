from PIL import Image
import numpy as np

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


print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

def calculation_brightness_to_character(number):
    index_lightness = 0
    if number <=254:
        index_lightness = number
    else:
        index_lightness = 256
    return index_lightness 

    
lightness = ("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$") 

l=[]
for elem in lightness:
    for i in range(4): #dont need define i in advance
        l.append(elem) #array l is the repeated character array




new_array = []         


for mem in number_light:
    index_new = calculation_brightness_to_character(mem)
    character = l[index_new]
    new_array.append(character)
print(new_array)     


print(new_array.index(";"))   
        