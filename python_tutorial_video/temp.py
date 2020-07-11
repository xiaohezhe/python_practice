import numpy as np
from numpy import pi,sin,cos,floor,ceil,sqrt

string ="Anne"
# "" express string
character_gender="her"
# can give the number value to the viable
character_age = "50.34234234"
print(string +", and " + character_gender + " age is " + character_age +"!")

phrase_upper = "HELLO WORLD!"
phrase_lower = "HELLO WORLD!"
print("hello\nworld!\n")
print(phrase_lower.upper() + " is cool ")
print("hello world!\"fsesfef")
print(phrase_upper.lower())
print(phrase_upper.islower())  # give the result of true or false
# after \ means output sth
# change the string to lower letter
# .upper/lower() is a function to change the letters
print(phrase_upper.lower().islower())
print(phrase_upper.lower()[0])  # output the first letter of lower phrase

# .index("")out put the number of the letter in a string
print(phrase_upper.lower().index("h"))
print(phrase_upper.lower().index(" "))

# .replace("old one","new one") is a replace function
phrase = "Giraffe Academy"
print(phrase)
print(phrase.replace("Giraffe Academy", "elephant"))

print(3 + 4.5)

# number should be converted to string first and next to string
# str() can convert a number to string
my_number = -5
print(str(my_number) + " my favorite number!")
print(abs(my_number))
print(pow(4,2))  # 4^2
print(max(4,2))
print(round(3.5))
print(round(3.4))
print(round(3.6))  # 四舍五入

print(floor(3.7))  # import math floor() is the function just get the lower number
print(ceil(3.7))
print(sqrt(36))

#####################################################
###########get input from others#####################

#name = input("Enter your name: ")
#print("Hello " + name + "!")



#####################################################
###########building a basic calculator###############

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")

#result = float(num1) + float(num2) # change string to decimal number

#print(result)


#####################################################
###########building a Mad Libs Game###############


#####################################################
################      lists           ###############

friends = ["Kevin","Karen","Jim","Oscar","Toby","Lily"]#0,1,2; -3,-2,-1
example = ["Kevin",2,False]
print(example)

print(friends[0],friends[2]) 

print(friends[-3]) 

print(friends[1:5]) #not included the index 5 name

friends[1]="Lucy"

print(friends)


#####################################################
################      lists    fuction       ###############

lucky_numbers = [14354,2,3,4,5,6,7,8]
friends = ["Kevin","Karen","Jim","Oscar","Toby","Lily"]

friends.extend(lucky_numbers) ##add another array to an array


friends.append(9)##add the last element of 9


friends.insert(1,"Ella")



friends.remove("Kevin")



friends.remove(2)

print(friends)

friends.pop()##delete the last element of an array

print(friends)

print(friends.index("Oscar"))##find the index of a specific element in array

friends.clear()
print(friends)


my_friends = ["Kevin","Karen","Jim","Jim","Oscar","Toby","Lily"]
print(my_friends.count("Jim"))##count Jim in array

my_friends.sort()#in increasing order output
lucky_numbers.sort()


print(my_friends)
print(lucky_numbers)

lucky_numbers.reverse()##output the elements from the last one to the first one
print(lucky_numbers)

friends2 = my_friends.copy()

print(friends2)


#####################################################
################      Tuples 元组 ###############
print("##########################################")
## the different between list and tuples is we can change the value in tuples
## but we can change the values in list
coordinates = (4,5)
print(coordinates[1])

coordinates_1 = [(4,5),(5,2),(546,342)]
coordinates_1[0]=(2342,32434)
print(coordinates_1)




#####################################################
################    Function  ###############
print("##########################################")




def say_hi(name,age) :# the code indented means it is inside the function
     print("Hello " + name + "!" + " you are " + str(age))
     

say_hi("Mike",35)   #call the function by the name with()
say_hi("Steve",16)



#####################################################
################    Return Statement  ###############
print("**********************************************")

def cube(number):
    print("hihi")
    return number * number *number
    
print(cube(3))
result = cube(4)    
print(result)




#####################################################
################    If Statement  ###############
print("**********************************************")

is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but you are tall")
else:
    print("you are not a male and not tall")


#####################################################
################ If Statement with comparison ###############
print("**********************************************")

def compare(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(compare(213231,213231,345))


#####################################################
################ Building a better calculator ###############
print("**********************************************")


cal1 = float(input("input the first number: "))

op = input("input the operator: ")

cal2 = float(input("input the second number: "))

if op == "+":
    print(cal1 + cal2)

elif op == "-":
    
    print(cal1 - cal2)

elif op == "%":
    print(cal1 % cal2)
    
else:
    print("invalid operator")
    
    
    
#####################################################
################ Dictionaries ###########  
    
monthConversion={
    1:"Jan",
    2:"Feb",
    3:"March",
    4:"April",
    "May":"May"
}
print(monthConversion.get(1))

print(monthConversion.get(5))

print(monthConversion.get(5),"not a valid key")


#####################################################
################ while loop ###########  

i =1
while i <= 10:
    print(i)
    i +=1
    
print(str(i) + " Done with loop")

#####################################################
################ Building a Guessing Game ########### 

secret_word = "giraffe"
guess = ""
i =1

while guess != secret_word and i <=3:
    guess = input("enter guess: ")
    i+=1
    
if(i <= 3):    
    print("You win!")
else:
    print("Game over!")


#####################################################
################ For loop ########### 
    

for letter in "Giraffe Academy":
    print(letter)

friends = ["Lucy","Ella","Cindy"]
for friend in friends:
    print(friend)
    
for index in range(len(friends)):
    print(friends[index])
    

for index in range(4):
    if index ==0:
        print("first iteration")
    elif index ==1:
        print("the 2nd iteration")
    elif index ==2:
        print("the 3rd iteration")
    else:
        print("the last iteration")
    
    
    
#####################################################
################Exponent Function 指数函数########### 
        
def raise_to_power(base_num, pow_num):       

    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))

#####################################################
################2D Lists & Nested Loops###########

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[3][0])

print("***********************************")

for row in number_grid:
    print(row)
    for col in row:##after finishing the inside loop and then start to continue to run the ouside loop
        print(col)
        
        
        
#####################################################
################Build a Translator###########   
        
#Giraffe Language
#vowels -> g
#------------------------

#dog -> dgg
#cat -> cgt    
print("***********************************")       
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G" 
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
          
    
####################################################
################     Except   ########### 

try:
    answer = 10/0
    number = int(input("input a number: "))
    print(number)
    
except ZeroDivisionError:
    print("divided by 0")    
except ValueError:
    print("invalid input")
    
## ZeroDivisionError and ValueError are for specific errors
    
####################################################
################  Modules & Pip  ########### 
import usefultools

print(usefultools.roll_dice(10))


####################################################
################  Class and objects   ########### 
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")    
#creating our own data type
from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 5, True)

print(student2.gpa)    
    
####################################################
################  Question quiz  ###########     
    
from question import Question

##creating the array of question prompts
question_prompts = [
    "what color are apples?\n (a) Red\n (b) Orange\n what's your answer?\n",
    "what color are Bananas?\n (a) Red\n (b) Yellow\n what's your answer?\n",  
    "what color are strawberries?\n (a) Red\n (b) Orange\n what's your answer?\n"
    ]#问题提示



##creating another array including the data type of Question 

questions = [
    Question(question_prompts[0], "a"),#Question object
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    ]
'''
##creating a function to show the question and let user to answer it
def run_test(questions):
    score = 0
 '''
score = 0
    ##question.prompt 是依次输出问题
    #使用input时会先显示问题，然后将用户输入的答案赋给answer
for question in questions:    
    answer = input(question.prompt)
    print("right answer is: " + question.answer + "\n") 
    if answer == question.answer:
        score += 1
    print("this turn, your score is: " + str(score))
print("final result is: " + str(score) + "/" + str(len(questions)))

 
    
####################################################
################  Object function ###########     
from student import Student


student1 = Student("Lucy","Art", 3.1, False)
student2 = Student("Lucy","Art", 3.9, True)

print(student1.on_honor_roll())
        
print(student2.on_honor_roll())


####################################################
################  Inheritance 继承 ###########  
    
from chef import Chef
from chinesechef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
myChineseChef.make_salad()
myChineseChef.make_special_dish()



####################################################
############# Python Interpreter 口译员 ###########    
     '''open a terminal'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    

    



