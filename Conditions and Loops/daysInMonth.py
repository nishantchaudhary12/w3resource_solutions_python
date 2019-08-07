#Write a Python program to convert month name to a number of days.


def convert(name):
    if name == "February":
        print("No. of days: 28/29 days")
    elif name in ("April", "June", "September", "November"):
        print("No. of days: 30 days")
    elif name in ("January", "March", "May", "July", "August", "October", "December"):
        print("No. of days: 31 day")
    else:
        print("Wrong month name")


convert('January')