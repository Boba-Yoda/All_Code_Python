#Operators 1
#Is a single equal sign an assigment operator
#Or an equality operator 
# ipynb - Interactive Python Notebook

song = 2+1
song = 3.0
song = "geese"
print(song)


#A single equal sign is an assigment operator

mysteryValue = type(5)
print(mysteryValue)
   
# A shorten way to find the data type
print(type(-10))


x= input("What is your name?")
y = input("What is your age?")

print("Hello", x)
print ("You are", y, "years old")

print(type(x))
print(type(y)) 


firstAge = input("What is the age of person 1?")
secondAge = input("What is the age of person 2?")

#The int function converts the strings firstAge and secondAge into integers
difference = int(firstAge) - int(secondAge)

print("Person 1 is", difference, "years old than person 2.")


pythonFunction = int(3.14149)
print(pythonFunction)

pythonFunction1 = str(8675309)
print(pythonFunction1)

pythonFunction2 = bool(0)
print(pythonFunction2)

pythonFunction3 = bool(1)
print(pythonFunction3)

pythonFunction4 = float(10)
print(pythonFunction4)


guess = int(input("Pick a number"))

if (guess<10):
    print("Too Low")
elif (guess == 10):
    print("Exactly 10")
else: 
    print("Too High") 

print(True) 
print(4==4) 
print(2+6==8) 
print(5!=120) 
print(2<4) 
print(4>=1)

# and operator 
sleep = 8         #Modify this number to see how it changes the output 
breakfast = True  #Modify this number to see how it changes the output 
print (sleep>=9 and breakfast==False) 

# or operator 
food = "cake"     #Modify this food to see how it changes the output 
print(food=="icecream" or food=="muffins") 

# not operator 
movie = "dislike"    #Modify this to say "dislike" to see how it changes the output 
print (movie!="like")

guesses = -1  # Change this number to see how the code output changes. 

if guesses >= 1: 
  x = int(input("pick a number:")) 
  if x < 10: 
    print("too low") 
  else: 
    print("too high") 
else: 
  print("You have run out of guesses!")
