sandwichType = input("Choose a sandwich type: 1. Chicken $5.25, 2. Beef $6.25, 3. Tofu $5.75")

if (sandwichType == "chicken"):
    print("Chicken $5.25")
    st = "Chicken $5.25"
    totalCost = 5.25
elif (sandwichType == "beef"):
    print("Beef $6.25")
    st = "Beef $6.25"
    totalCost = 6.25
elif (sandwichType == "tofu"):
    print("Tofu $5.75")
    st = "Tofu $5.75"
    totalCost = 5.75

drinkType = input("Would you like a drink?")
ds = ""
if (drinkType == "yes"):
    drinkSize = input("Which size would you like: 1. Small $1.00 2. Medium $1.75 3. Large $2.25")
    if (drinkSize == "small"):
        print("Small $1.00")
        ds = "Small $1.00"
        totalCost = totalCost + 1
    elif (drinkSize == "medium"):
        print("Medium $1.75")
        ds = "Medium $1.75"
        totalCost = totalCost + 1.75
    elif (drinkSize == "large"):
        print("Large $2.25")
        ds = "Large $2.25"
        totalCost = totalCost + 2.25

friesType = input("Would you like a fries?")
fs = ""
if (friesType == "yes"):
    friesSize = input("Which size would you like: 1. Small $1.00 2. Medium $1.50 3. Large $2.00")
    if (friesSize == "small"):
        megaSize = input("Would you like to mega-size your fries")
        if (megaSize == "yes"):
            print("Large $2.00")
            fs = "Large $2.00"
            totalCost = totalCost + 2
        else:    
            print("Small $1.00")
            fs = "Small $1.00"
            totalCost = totalCost + 1
    elif (friesSize == "medium"):
        print("Medium $1.50")
        fs = "Medium $1.50"
        totalCost = totalCost + 1.5
    elif (friesSize == "large"):
        print("Large $2.00")
        fs = "Large $2.00"
        totalCost = totalCost + 2

ketchupPackets = int(input("How many ketchup packets would you like, they are 25 cents each?"))
totalCost = 0.25 * ketchupPackets + totalCost

if (drinkType == "yes" and friesType == "yes"):
    print("You got a discount because you ordered, fries, a drink, and a sandwich!")
    totalCost = totalCost - 1

print ("You ordered", st, ds, fs)
print("You total cost is $", totalCost)
