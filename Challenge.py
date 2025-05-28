def challenge(arg1):
  if type(arg1) == str:
    print(type(arg1))
    print(arg1)
    arg1 = str(arg1) + "!" 
    return (arg1)
  elif type(arg1) == int:
    print(type(arg1))
    print(arg1)
    arg1 = arg1 + 5
    return (arg1)
  elif type(arg1) == float:
    print(type(arg1))
    print(arg1)
    arg1 = arg1 + 3.13
    return (arg1)
  elif type(arg1) == bool:
    print(type(arg1))
    print(arg1)
    arg1 = arg1 + True
    if arg1 == 0:
     arg1 = False
    else:
      arg1 = True
    
    return (arg1)

print(challenge("hi"))
print(challenge(5))
print(challenge(3.14))
print(challenge(False))
