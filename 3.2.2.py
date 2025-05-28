#To create a class, use the keyword class:
class MyClass:
  x = 5

#Create an object named p3, and print the value of x:
p3 = MyClass()
print(p3.x)

#Create a class named Person, use the __init__() function to assign values for name and age:
#The __init__() function is called automatically every time the class is being used to create a new object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
    
print(p1.name)
print(p1.age) 
