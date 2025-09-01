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
#My fourth lab introducing the list data type defining a list
myFruitList =["apple","banana","cherry"]
print(myFruitList)
print(type(myFruitList))
#Accessing a list by postion
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
#changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)
#Introducing the tuple data type
myFinalAnswerTuple =("apple","banana","pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
#Accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
#Introducing the dictionary data type
myFavoriteFruitDictionary = { "Akua": "apple","Saanvi" : "banana", "paulo" : "pineapple" }
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
#Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["paulo"])
#My Fifth lab Categorizing Values
myMixedTypeList =[45,290578,1.02,True,"My dog is on the bed.","45"]
for item in myMixedTypeList:
    print("{} is of the data type {}". format(item,type(item)))