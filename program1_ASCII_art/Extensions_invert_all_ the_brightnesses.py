# =============================================================================
# change the text color and background color, put the file in the C:\Users\15695
# using Terminal in Spider open it 
# =============================================================================
from colorama import init, Fore, Back, Style
# =============================================================================
# Convert brightness numbers to ASCII characters
# =============================================================================

from PIL import Image
import numpy as np

#open image
im = Image.open("pineapple.jpg")
w,h=im.size
#python里//表示取整除，返回商的整数部分（向下取整）
w=w
h=h

im=im.resize((w,h))
#im.show()

data = list(im.getdata())#list all the tuples of grids
data_2_dimensional = np.array(im)
wide = (data_2_dimensional).shape
print(wide)  #(467, 700, 3)



# =============================================================================
# array l is the repeated character array
# =============================================================================
lightness = ("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$") 

l=[]
for elem in lightness:
    for i in range(4): #dont need define i in advance
        l.append(elem) #array l is the repeated character array
        
        
# =========================================================================================================
# setting to chose average/min_max/luminosity mappings and get the sigle brightness value array
# =========================================================================================================

number_map = []

chose_user = "luminosity"
number_value = 0

for x in range(wide[0]):
    for y in range(wide[1]):
        R = data_2_dimensional[x,y][0]
        G = data_2_dimensional[x,y][1]
        B = data_2_dimensional[x,y][2]
        if chose_user == "average":
            number_value = int((R + G + B) / 3)
        elif chose_user == "min_max":     
            number_value = int((max(R, G, B) + min(R, G, B)) / 2)
        elif chose_user == "luminosity": 
            number_value = int(0.21*R + 0.72*G + 0.07*B)
       
        number_map.append(number_value)
        
print(number_map)
print(Back.LIGHTCYAN_EX +"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print(Back.LIGHTCYAN_EX +"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print(Back.LIGHTCYAN_EX +"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print(Back.LIGHTCYAN_EX +"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print(Back.LIGHTCYAN_EX +"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print(Back.LIGHTCYAN_EX +"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")        
# print(len(number_map))#326900
# =============================================================================
# change the arrry order to invert the brightness
# =============================================================================

invert_number_map = []

for j in range(326899,-1,-1):#from the index of 326899 to decress and output the number
    invert_number_map.append(number_map[j])

# print(invert_number_map)
# print(len(invert_number_map))





# =============================================================================
#  turn brightness inversion on and off
# =============================================================================

last_number_map = []
turn_on = False
if turn_on:
    last_number_map = invert_number_map
else:
    last_number_map = number_map



print(last_number_map)










# =============================================================================
# function is the math measure to map character and pixel changed number
# =============================================================================
def calculation_brightness_to_character(number):
    index_lightness = 0
    if number <=254:
        index_lightness = number
    else:
        index_lightness = 256
    return index_lightness 


# =============================================================================
# map average number and character
# =============================================================================
j=0
new_array = []     
   
for mem in number_map:
    for i in range(3):
        index_new = calculation_brightness_to_character(mem)#output every charactore 3 times to avoid the squashed problem
        character = l[index_new]
        new_array.append(character)
        j +=1
#output 100 charaters change next line
        if j == w*3:
            new_array.append("\n")
            j=0

# =============================================================================
# output the result as a whole string and change the color of text
# =============================================================================    
# str=""
# print(str.join(new_array))     #output the array as string

#turn off color changes at the end of every print, coloar change only works for the pointed sentence or word
#init(autoreset=True)

# =============================================================================
# print(Fore.MAGENTA + 'some red text')--品红
# print('automatically back to default color again')
# print(Back.GREEN + 'and with a green background')
# print(Back.CYAN + 'and with a green background')--青色
# print('automatically back to default background again')
# print(Back.RESET + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# =============================================================================
#print(Fore.YELLOW + str.join(new_array))
#print(Back.LIGHTCYAN_EX +  str.join(new_array))




# =============================================================================
# change RGB to average and get the average array number_average[]
# =============================================================================
# number_average = []
# for x in range(wide[0]):
#     for y in range(wide[1]):
#         R = data_2_dimensional[x,y][0]
#         G = data_2_dimensional[x,y][1]
#         B = data_2_dimensional[x,y][2]
#         average = int((R + G + B) / 3)
#         number_average.append(average)
       
#print(number_average) #number_average is the array of single brightness values 


# =============================================================================
# change RGB to min_max and get the min_max array number_min_max[]
# =============================================================================
# number_min_max= []
# for x in range(wide[0]):
#     for y in range(wide[1]):
#         R = data_2_dimensional[x,y][0]
#         G = data_2_dimensional[x,y][1]
#         B = data_2_dimensional[x,y][2]
#         min_max = int((max(R, G, B) + min(R, G, B)) / 2)
#         number_min_max.append(min_max)

# =============================================================================
# change RGB to luminosity and get the luminosity array number_luminosity[]
# =============================================================================
# number_luminosity= []
# for x in range(wide[0]):
#     for y in range(wide[1]):
#         R = data_2_dimensional[x,y][0]
#         G = data_2_dimensional[x,y][1]
#         B = data_2_dimensional[x,y][2]
#         luminosity = int(0.21*R + 0.72*G + 0.07*B)
#         number_luminosity.append(luminosity)


    
# =============================================================================
# output the result as a whole string and change the color of text
# =============================================================================    
#str=""
#print(str.join(new_array))     #output the array as string

#turn off color changes at the end of every print, coloar change only works for the pointed sentence or word
#init(autoreset=True)

# =============================================================================
# print(Fore.MAGENTA + 'some red text')--品红
# print('automatically back to default color again')
# print(Back.GREEN + 'and with a green background')
# print(Back.CYAN + 'and with a green background')--青色
# print('automatically back to default background again')
# print(Back.RESET + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# =============================================================================
#print(Fore.YELLOW + str.join(new_array))
#print(Back.LIGHTCYAN_EX +  str.join(new_array))






