#write a program code in python to take first name and last name from user and print full name if the length of the full name is
#less than 12 otherwise print invalid name

first_name = input("enter first name of student")
last_name = input("enter last name of student")
full_name = first_name+last_name
if(len(full_name) >12):
    print("Invalid name")
else:
    print("the name is",full_name)
