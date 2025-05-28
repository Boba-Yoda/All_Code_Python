#Python function that prnts out the text in the
#parameter and adds an ! mark

def excitedPrintText(stringToPrint):
    print(stringToPrint + "!")
    print (stringToPrint, "!")

excitedPrintText("Hello")

#Tester Code
dataType = int(input("Pick a number from 1-4! 1- String 2- Integer 3- Float 4- Boolean "))

if (dataType == 1):
    print("You picked 1 - string")
elif (dataType == 2):
    print("You picked 2- integer")
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("The sum of your numbers are", num1 + num2)
    print("The difference of your numbers are", num1 - num2)
    print("The product of your numbers are", num1 * num2)
    print("The quotient of your numbers are", num1 / num2)
elif (dataType == 3):
    print("You picked 3 - float")
elif (dataType ==4):
    print("You picked 4- boolean")
else: 
    print("Enter a number from 1-4") 




def challenge(arg1):
  
  if type(arg1) == str:
    x= input("Type your favorite food")
    print(type(arg1))
    arg1 = str(x) + "!" 
    return (arg1)
  elif type(arg1) == int:
    y= int(input("Type your favorite number"))
    print(type(arg1))
    arg1 = y + 5
    return (arg1)
  elif type(arg1) == float:
    print(type(arg1))
    z = float(input("Type your birthday in the format of 00.00"))
    arg1 = z + 3.13
    return (arg1)
  elif type(arg1) == bool:
    print(type(arg1))
    m = bool(input("Type true or false"))
    arg1 = m + True
    if arg1 == 0:
     arg1 = False
    else:
      arg1 = True
    
    return (arg1)

print(challenge("hi"))
print(challenge(5))
print(challenge(3.14))
print(challenge(False))
