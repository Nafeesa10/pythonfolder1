# My first python program
print("Hello,World")
#My second python program
print("python has three numeric types: int,float,complex")
#creating a variable
myvalue=1
print(myvalue)
print(type(myvalue))
print(str(myvalue) + " is of the data type "+ str(type(myvalue)))
#Introducing the float data type
myvalue=3.14
print(myvalue)
print(type(myvalue))
print(str(myvalue) + "is of the data type"+ str(type(myvalue)))
#introducing the complex data type
myvalue=5j
print(myvalue)
print(type(myvalue))
print(str(myvalue) + "is of the data type" + str(type(myvalue)))
#introducing the boolan data type for True
myvalue=True
print(myvalue)
print(type(myvalue))
print(str(myvalue) + "is of the data type" + str(type(myvalue)))
#introducing the boolan data type for false
myvalue=False
print(myvalue)
print(type(myvalue))
print(str(myvalue) +" is of the data type" + str(type(myvalue)))
# My third lab intrducing the string data type
mystring = "This is a string"
print(mystring)
print(type(mystring))
print(mystring + "is of the data type "+ str(type(mystring)))
#Working the string concatenation
firststring = "water"
secondstring ="fall"
thirdstring ="firststring +secondstring"
print(thirdstring)
#working with input strings
name = input("what is your name?")
print(name)
# Formatting output strings
color =input("what is your favorite color?")
animal =input("what is your favorite animal?")
print(" {}, you like a {} {}!".format(name,color,animal))
