def endProgram():
    sandwich = ["chicken", "beef", "tofu"]
    drink = ["small", "medium", "large"]
    fries = ["small", "medium", "large"]

    dir(sandwich)
    dir(drink)
    dir(fries)

    order = []

    def sandwichChecker(totalCost):
        while True:
            sandwichType = input("Choose a sandwich type: 1. Chicken $5.25, 2. Beef $6.25, 3. Tofu $5.75")
            if sandwichType in sandwich:
                if (sandwichType == "chicken"):
                    print("Chicken $5.25")
                    try:
                        st = int(input("How many chicken sandwiches would you like?"))
                        if type(st) == int or 0:
                            if st > 0:
                                totalCost = totalCost + 5.25 * st
                                while st>0:
                                    order.append("chicken")
                                    st = st - 1  
                                break
                            elif st == 0:
                                order.remove("chicken")
                            else:
                                print("That input is not excepted try again")
                    except ValueError:
                        print("That is not a number try again")
                    
                elif (sandwichType == "beef"):
                    print("Beef $6.25")
                    try:
                        bt = int(input("How many beef sandwiches would you like?"))
                        if type(bt) == int:
                            if bt > 0:
                                totalCost = totalCost + 6.25 * bt
                                while bt>0:
                                    order.append("beef")
                                    bt = bt -1   
                                break
                            elif bt == 0:
                                order.remove("beef")
                                break
                            else:
                                print("That input is not excepted try again")
                    except ValueError:
                        print("That is not a number try again")
                
                elif (sandwichType == "tofu"):
                    print("Tofu $5.75")
                    try:
                        tt = int(input("How many tofu sandwiches would you like?"))
                        if type(tt) == int or 0:
                            if tt > 0:
                                totalCost = totalCost + 5.75 * tt
                                while tt>0:
                                    order.append("tofu")
                                    tt = tt -1
                                break
                            elif tt == 0:
                                order.remove("tofu")
                                break
                            else:
                                print("That input is not excepted try again")
                    except ValueError:
                        print("That is not a number try again")  
            else:
                print("That's not on the menu. Please try again.")

        return totalCost

    def drinkChecker(totalCost, drinkType):
        while True:
            drinkType = input("Would you like a drink?")
            if (drinkType == "yes"):
                drinkSize = input("Which size would you like: 1. Small $1.00 2. Medium $1.75 3. Large $2.25")
                if drinkSize in drink:
                    if (drinkSize == "small"):
                        print("Small $1.00")
                        try:
                            ds = int(input("How many small drinks would you like?"))
                            if type(ds) == int or 0:
                                if ds > 0:
                                    totalCost = totalCost + 1 * ds
                                    while ds>0:
                                        order.append("small drink")
                                        ds = ds -1   
                                    break
                                elif ds == 0:
                                    order.remove("small drink")
                                    break
                                else:
                                    print("That input is not excepted try again")
                        except ValueError:
                            print("That is not a number try again")  
                
                    elif (drinkSize == "medium"):
                        print("Medium $1.50")
                        try:
                            dm = int(input("How many medium drinks would you like?"))
                            if type(dm) == int or 0:
                                if dm > 0:
                                    totalCost = totalCost + 1.5 * dm
                                    while dm>0:
                                        order.append("medium drink")
                                        dm = dm -1   
                                    break
                                elif dm == 0:
                                    order.remove("medium drink")
                                    break
                                else:
                                    print("That input is not excepted try again")
                        except ValueError:
                            print("That is not a number try again")  
                
                    elif (drinkSize == "large"):
                        print("Large $2.25")
                        try:
                            dl = int(input("How many large drinks would you like?"))
                            if type(dl) == int or 0:
                                if dl > 0:
                                    totalCost = totalCost + 2.25 * dl
                                    while dl>0:
                                        order.append("large drink")
                                        dl = dl -1   
                                    break
                                elif dl == 0:
                                    order.remove("large drink")
                                    break
                                else:
                                    print("That input is not excepted try again")
                        except ValueError:
                            print("That is not a number try again")  
                
                else:
                    print("That's not on the menu. Please try again.")
            else:
                break

        return totalCost, drinkType

    def friesChecker(totalCost, friesType):
        while True:
            friesType = input("Would you like fries?")
            if (friesType == "yes"):
                friesSize = input("Which size would you like: 1. Small $1.00 2. Medium $1.50 3. Large $2.00")
                if friesSize in fries:
                    if (friesSize == "small"):
                        megaSize = input("Would you like to mega-size your fries?")
                        if (megaSize == "yes"):
                            print("Large $2.00")
                            try:
                                fl = int(input("How many large fries would you like?"))
                                if type(fl) == int or 0:
                                    if fl > 0:
                                        totalCost = totalCost + 2 * fl
                                        while fl>0:
                                            order.append("large fries")
                                            fl = fl -1   
                                        break
                                    elif fl == 0:
                                        order.remove("large fries")
                                        break
                                    else:
                                        print("That input is not excepted try again")
                            except ValueError:
                                print("That is not a number try again")  
                        
                        else:
                            print("Small $1.00")
                            try:
                                fs = int(input("How many small fries would you like?"))
                                if type(fs) == int or 0:
                                    if fs > 0:
                                        totalCost = totalCost + 1 * fs
                                        while fs>0:
                                            order.append("small fries")
                                            fs = fs -1   
                                        break
                                    elif fs == 0:
                                        order.remove("small fries")
                                        break
                                    else:
                                        print("That input is not excepted try again")
                            except ValueError:
                                print("That is not a number try again")
                           
                    elif (friesSize == "medium"):
                        print("Medium $1.50")
                        try:
                            fm = int(input("How many medium fries would you like?"))
                            if type(fm) == int or 0:
                                if fm > 0:
                                    totalCost = totalCost + 1.5 * fm
                                    while fm>0:
                                        order.append("medium fries")
                                        fm = fm -1   
                                    break
                                elif fm == 0:
                                    order.remove("medium fries")
                                    break
                                else:
                                    print("That input is not excepted try again")
                        except ValueError:
                            print("That is not a number try again")
                       
                    elif (friesSize == "large"):
                        print("Large $2.00")
                        try:
                            fl = int(input("How many large fries would you like?"))
                            if type(fl) == int or 0:
                                if fl > 0:
                                    totalCost = totalCost + 2 * fl
                                    while fl>0:
                                        order.append("large fries")
                                        fl = fl -1   
                                    break
                                elif fl == 0:
                                    order.remove("large fries")
                                    break
                                else:
                                    print("That input is not excepted try again")
                        except ValueError:
                            print("That is not a number try again")  
                        
                else:
                    print("That's not on the menu. Please try again.")
            else:
                break

        return totalCost, friesType
    
    
    def ketchupChecker(totalCost):
        while True:
            try:
                ketchup = int(input("How many ketchup packets would you like?"))
                if type(ketchup) == int:
                    if ketchup > 0:
                        totalCost = totalCost + 0.25 * ketchup
                        order.append(ketchup)
                        break
                    elif ketchup == 0:
                        break
                    else:
                        print("That input is not excepted try again")
            

            except ValueError:
                print("That is not a number try again")
    
        return(totalCost) 

    totalCost = 0
    drinkType = ""
    friesType = ""
    totalCost = sandwichChecker(totalCost)
    totalCost, drinkType = drinkChecker(totalCost, drinkType)  
    totalCost, friesType = friesChecker(totalCost, friesType)
    totalCost = ketchupChecker(totalCost)


    if drinkType == "yes" and friesType == "yes":
        totalCost = totalCost - 1
        print("You got a $1 discount for ordering a sandwich, drink, and fries!")


    print("Your order is", order)
    print("Your total is $", totalCost)

    program = input("Are you happy with your order?")

    if (program == "yes"):
        print("Thank you, your order has been placed!")
        return
    else:
        print("It's okay, restarting the ordering process")
        return endProgram()

endProgram()
