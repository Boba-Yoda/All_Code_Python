trys = 5

def endProgram(trys):
    options = ["A Day At The Beach", "The Worst Summer Camp Ever", "Summer Roadtrip Gone Wrong", "How To Survive A Heatwave", "My Crazy Summer Job"]

    dir(options)

    print("Welcome to the Mad Libs Games")
    print("All options are summer themed and you have 5 trys to play")
    print("Enter in the correct words to fit the prompts, just know that if you mess it up you are only messing up the fun for yourself")
    print("Here are the options you can choose from", options)
    def madLibs():
        while True:
            madLibType = input("Choose an Mad Lib topic to begin ")
            if madLibType in options:
                if madLibType == "A Day At The Beach":
                    adjective = input("Adjective: ")
                    personsName = input("Person's Name: ")
                    noun = input("Noun: ")
                    pluralNoun = input("Plural Noun: ")
                    texture = input("Texture: ")
                    bodyParts = input("Plural Body Part: ")
                    liquid = input("Liquid: ")
                    clothingItem = input("Clothing Item: ")
                    animal = input("Animal: ")
                    clothingItem2 = input("Clothing Item: ")
                    householdObject = input("Household Object: ")
                    food = input("Food: ")
                    beverage = input("Beverage: ")
                    noun2 = input("Noun: ")
                    exclamation = input("Exclamation (In quotes): ")
                    celebrity = input("Celebrity: ")
                    naturalFeature = input("Natural Feature: ")
                    print("Yesterday, I went to the beach with my", adjective, "friend", personsName,".")                   
                    print("We brought a giant", noun, "and", pluralNoun, "for entertainment.")
                    print("The sand felt like", texture, "under our", bodyParts, ".")
                    print("While sunbathing, I accidentally spilled", liquid, "on my", clothingItem, ".")
                    print("We decided to build a sandcastle shaped like a", animal, "wearing a", clothingItem2, ".")
                    print("Then we played beach volleyball using a", householdObject, "instead of a ball.")
                    print("For lunch, we had", food, "and drank" , beverage, ".")
                    print("Later, a seagull tried to steal my", noun2, "and I had to chase it while screaming,", exclamation, "!")
                    print("As the sun set, we took a photo with a random", celebrity, "we met by the", naturalFeature, ".")
                    print("Best Beach Day Ever!")
                    break
                
                elif madLibType == "The Worst Summer Camp Ever":
                    sillyName = input("Silly Name: ")
                    weirdPhrase = input("Weird Phrase (In quotes): ")
                    number = input("Number: ")
                    pluralNoun = input("Plural Noun: ")
                    material = input("Material: ")
                    smellyThing = input("Smelly Thing: ")
                    name = input("Name: ")
                    verbing = input("Verb ending in -ing: ")
                    grossFood = input("Gross Food: ")
                    pluralNoun2 = input("Plural Noun: ")
                    pluralNoun3 = input("Plural Noun: ")
                    animal = input("Animal: ")
                    plumbingItem = input("Plumbing Item: ")
                    warningMessage = input("Warning Message (In quotes): ")
                    adjective = input("Adjective: ")
                    mythicalCreature = input("Mythical Creature: ")
                    oldMovie = input("Old Movie: ")
                    randomObject = input("Random Object: ")
                    shape = input("Shape: ")
                    funnyAdvice = input("Funny Advice (In quotes): ")
                    print("Welcome to Camp", sillyName, "where the motto is", weirdPhrase, ".")                   
                    print("On day one, I got assigned to Cabin", number, "with a bunch of", pluralNoun, ".")
                    print("The beds were made of", material, "and smelled like", smellyThing, ".")
                    print("Our counselor,", name, "told us that instead of swimming, we’d be", verbing, "in the mud.")
                    print("The mess hall served things like", grossFood, "with a side of", pluralNoun2, ".")
                    print("During arts and crafts, we glued", pluralNoun3, "onto a live", animal, ".")
                    print("The bathroom had one working", plumbingItem, "and a sign that read,", warningMessage, ".")
                    print("I made friends with a", adjective, "kid who claimed they saw a", mythicalCreature, "in the woods.")
                    print("Our evening activity was watching", oldMovie, "on a sheet using a flashlight and a", randomObject, ".")
                    print("By the end of the week, I had a rash shaped like", shape, "and a letter from home that just said," ,funnyAdvice, ".")
                    print("Next year, I’m staying home.")
                    break
                
                elif madLibType == "Summer Roadtrip Gone Wrong":
                    city = input("City: ")
                    place = input("Faraway Place: ")
                    vehicleType = input("Vehicle Type: ")
                    pluralFood = input("Plural Food: ")
                    beverage = input("Beverage: ")
                    animal = input("Animal: ")
                    vehiclePart = input("Vehicle Part: ")
                    town = input("Random Town: ")
                    tool = input("Tool: ")
                    pluralNoun = input("Plural Noun: ")
                    adjective = input("Adjective: ")
                    pluralItem = input("Plural Item: ")
                    celebrity = input("Celebrity: ")
                    pluralNoun2 = input("Plural Noun: ")
                    valuableItem = input("Valuable Item: ")
                    noun = input("Noun: ")
                    print("This summer, we planned a road trip from", city, "to", place, "in our old", vehicleType, ".")                   
                    print("We packed snacks like", pluralFood, "and loaded up on", beverage, ".")
                    print("My sibling insisted on bringing their emotional support", animal, ".")
                    print("Everything was great until the", vehiclePart, "fell off somewhere near", town, ".")
                    print("We stopped to fix it using only duct tape, a", tool, "and", pluralNoun, ".")
                    print("Later, we accidentally drove into a", adjective, "parade, where we were pelted with", pluralItem, ".")
                    print("At a gas station, we met someone who claimed to be", celebrity, "in disguise.")
                    print("They gave us directions that led to a field full of", pluralNoun2, "and absolutely no roads.")
                    print("Eventually, we made it to our destination… but realized we left our", valuableItem, "at home.")
                    print("We laughed, cried, and vowed never to trust", noun, "again.")
                    break
                
                elif madLibType == "How To Survive A Heatwave":
                    adjective = input("Adjective: ")
                    noun = input("Noun: ")
                    material = input("Material: ")
                    pluralFood = input("Plural Food: ")
                    pluralNoun = input("Plural Noun: ")
                    electronicDevice = input("Electronic Device: ")
                    liquid = input("Strange Liquid: ")
                    container = input("Container: ")
                    pluralNoun2 = input("Plural Noun: ")
                    slipperyItem = input("Slippery Item: ")
                    clothingItem = input("Clothing Item: ")
                    pluralAnimal = input("Plural Animal: ")
                    randomObject = input("Random Object: ")
                    exclamation = input("Exclamation (In quotes): ")
                    pluralNoun3 = input("Plural Noun: ")
                    appliance = input("Appliance: ")
                    store = input("Store: ")
                    name = input("Name: ")
                    print("When summer hits and it’s hotter than a", adjective, noun, "here’s how to stay cool:")                   
                    print("First, wear a hat made of", material, "and fill your pockets with frozen", pluralFood, ".")
                    print("Build a fort out of", pluralNoun, "and hide inside with your favorite", electronicDevice, ".")
                    print("Instead of drinking water, sip on", liquid, "served in a", container, ".")
                    print("Replace all your furniture with inflatable", pluralNoun2, "and slide around on", slipperyItem, ".")
                    print("Do not, under any circumstances, wear", clothingItem, "they attract" , pluralAnimal, ".")
                    print("If you need to go outside, carry a", randomObject, "and yell", exclamation, "every 10 minutes for safety.")
                    print("Create a fan by taping", pluralNoun3, "to a ceiling", appliance, ".")
                    print("If it gets unbearable, go to the nearest", store, "and jump into their display pool.")
                    print("Lastly, write a strongly worded letter to the sun and sign it,", name, "the Overheated.")
                    break
                
                elif madLibType == "My Crazy Summer Job":
                    occupation = input("Occupation: ")
                    place = input("Place: ")
                    emotion = input("Emotion: ")
                    adjective = input("Adjective: ")
                    costume = input("Costume: ")
                    pluralItem = input("Plural Item: ")
                    name = input("Name: ")
                    quote = input("Strange Quote (In quotes): ")
                    verb = input("Verb: ")
                    object = input("Object: ")
                    food = input("Questionable Food: ")
                    musician = input("Musician: ")
                    animal = input("Animal: ")
                    pluralNoun = input("Plural Noun: ")
                    appliance = input("Appliance: ")
                    cleaningItem = input("Cleaning Item: ")
                    figure = input("Authority Figure: ")
                    letter = input("Letter: ")
                    disaster = input("Disaster: ")
                    activity = input("Activity: ")
                    pluralObject = input("Plural Objects: ")
                    material = input("Material: ")
                    print("This summer, I got a job as a", occupation, "at", place, "and it’s been pure", emotion, ".")
                    print("On day one, I was asked to wear a", adjective, costume, "and hand out", pluralItem, "to strangers.")
                    print("My boss", name, "told me the company motto was", quote, "." )
                    print("One coworker tried to teach me how to", verb, "while balancing on a", object, ".")
                    print("During lunch, we ate", food, "and listened to", musician, "on repeat")
                    print("Part of my job involved chasing a", animal, "that had escaped from the break room.")
                    print("I also had to clean", pluralNoun, "out of the", appliance, "using only", cleaningItem, ".")
                    print("One day, we had a surprise inspection by a", figure, "who gave us a grade of", letter, ".")
                    print("To celebrate surviving the week, I accidentally started a", disaster, "during a team-building of", activity, ".")
                    print("Still, I got paid in", pluralObject, "and earned the Employee of the Month crown made of", material, ".")
                    print("It was the best weird job I'll never do again.")
                    break

            else:
                print("That is not an option try again")             
    madLibs()

    program = input("Are you done playing Mad Libs, type yes to stop anything else will make you play again ")

    if program == "yes":
        print("Thank you for playing!")
        return
    else:
        while trys > 0:
            trys = trys - 1
            if trys == 0:
                print("Your trys are done thanks for playing!")
                return
            else:
                print("Okay time for more fun! You have", trys, "trys left")
                return endProgram(trys)

endProgram(trys)
