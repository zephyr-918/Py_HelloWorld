print("\nHello World!")
print("\nThis is Zephyr's first ever Python Code file that's synced to GitHub!")

current_year = input("\nWhich year is this? : ")
if current_year == 2020:
    print("\nThis is a hard year isn't it. Hope the Covid Ends quick! Alright, let's get to know more about you now :)")
else:
    print("\nOof, 2020 was a rough patch, I'm happy we're past that now. Alright, let's get to know more about you "
          "now :)")

    proceed = input("\n\nShall we proceed? [Y/N]: ")

if proceed == "Y" or "y":
    name = input("\nPlease enter your name here: ")
    age1 = input("\nWhich year were you born in?: ")
    age = int(current_year) - int(age1)
    print("Hello " + name + ". Pleasure to meet you!")
    if int(age) <= 13:
        print("\nYou come under the category of PG-13, meaning - you need to have parental guidance for certain "
              "actions to be taken on the Internet.")

    elif int(age) >= 18:
        print("\nYou're above 18, you're an adult now, be responsible and do not fall prey to your attractions unless "
              "they're worthy! :)")

    else:
        print("\nYou're in your Teen ages, be careful not to fall prey for any attractions you might come across.")

        print("\nThanks for answering to me, have a good day ;)\n")

elif proceed == "N" or "n":
    print("\n Ah! no big deal, Have a good day :)\n")

else:
    print('Invalid Response, the program will be closed!')

# This is a Comment.
