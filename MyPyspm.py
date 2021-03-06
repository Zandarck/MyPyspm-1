import sys
""" My Py Strong Password Maker.
If you are familar with python, please skip to the bottom to "grab and go" the needed code.
Comments and exmples are intended for people less familar.

This file contains a blank template.
An exmaple template with instructions.
And finally in the only uncommented space is the actual code.
"""

"""  <<Remove these quotes and all text within up until -- marker
Assign your own values for desired password strength.
Remeber to add more items in print section.
ex: print(items[], items[])  use comma and repeat itmes[] desired
amount of times --


items = ("", "", "", "", "", "", "", "", "", "",)

a = int(input("What numbers do you want to use? "))
b = int(input("Second number "))
c = int(input("Third number "))
print (items[a] + items[b] + items[c])

-- Also remove these quotes to use  >>>"""

"""Example using numbers 5 9 7 to create password for site
called eggedspam.dotcom

items = ("Vb@", "1X", "A8n", "x9*", "c!k", "b99", "hbOr", "kLm", "a#4", "h2",)

a = int(input("First number you want to use? ")) = 5
b = int(input("Second number ")) = 7
c = int(input("Third number ")) = 9

print (items[a] + items[b] + items[c])


Your password for eggedspam.dotcom is b99h2kLm
You can think of your password for this site as 597 and simply
run the program anytime you log in.
It's safer to enter your secret number into the program rather than writing down
the actual password or saving it to a file.
"""


items = (
    "x3#1c", "b7^X4", "jM88k", "c2^vB", "l!19d", "hB7&n", "v4$Ka",
    "mIkL7", "i8N4a", "vVb8&",
)

while True:
    choiceA = input("Would you want to access a random password: (Y/N) ").upper()
    if choiceA == "Y":
        print("Enter your 3 Digit pin: ")
        a = int(input("First number you want to use?: "))
        b = int(input("Second number you want to use?: "))
        c = int(input("Third number you want to use?: "))
        try:
            print(items[a] + items[b] + items[c])
        except IndexError:
            print("Values can only be from 0 through 9! Please try again")
    elif choiceA == "N":
        print("Shutting down...")
        sys.exit()


"""
Here is a template for creating a 15 digit password from three letters
!!Modify each item in some way for your security!!
To use this template remove triple quotes around
this template. Run the file and follow prompts.
Once a password has been created for a site using this do not
change values unless you have password recovery options.
"""
