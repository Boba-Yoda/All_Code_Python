#Activity 3.2.2 Step 7
from Post import Post

all_posts_archive = []

# your code here



options = ["new", "remove", "change user", "print", "quit"]
print(options)

def optionsChecker():
  while True:
    optionType = input("Choose an option from above ")
    if optionType in options:
        if optionType == "new":
            post1 = Post(input("Add first part of post here "), input("Add second part of post here "))
            print (post1)
            all_posts_archive.append(post1)
        elif optionType == "remove":
            print("You have", len(all_posts_archive), "posts")
            try:
              index = int(input("Which post would you like to delete? "))
              if index >= 0 and index < len(all_posts_archive):
                del all_posts_archive[index]
              else:
                print("Please enter a valid index (0 to " + str(len(all_posts_archive) - 1) + ")")
            except ValueError:
              print("Please enter a valid whole number.")
        elif optionType == "change user":
          username = input("What is your username ")
          print("Welcome", username)
        elif optionType == "print":
           for post in all_posts_archive:
            print(post)
        elif optionType == "quit":
           print("Goodbye, the program has ended")
           break
    else:
        print("That's not an option. Please try again.")

optionsChecker()
