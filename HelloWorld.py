print("\nHello World!")
print("\nThis is Zephyr's first ever Python Code file that's synced to GitHub!")

current_year = input("\nWhich year is this? : ")
if(current_year == 2020):
    print("\nThis is a hard year isn't it. Hope the Covid Ends quick! Alright, let's get to know more about you now :)")
else:
    print("\nOof, 2020 was a rough patch, I'm happy we're past that now. Alright, let's get to know more about you now :)")

proceed = input("\n\nShall we proceed? [Y/N]: ")

if(proceed == str('Y') or str('y')):
    name = input("\nPlease enter your name here: ")
    age = input("\nWhich year were you born in?: ")
    age2 = int(current_year) - int(age)
    if(int(age2) > 18):
        print("\nHello " + name + ". It's nice to meet you, I see that you're older than 18 now, you're a grown-up!")
    else:
        print("\nHello " + name + ". It's nice to meet you, I see that you're a young lad, I'm a young one aswell, let's be friends :) ")

    print("\nThanks for answering to me, have a good day ;)\n")
else:
    print("\n Ah! no big deal, Have a good day :)\n")
    exit()