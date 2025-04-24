#11. Write a program code in Python to take a string from the user and check whether the string is  palindrome or not
statement=input("enter any string to check palindrome")
new_string = statement[::-1]
if(new_string==statement):
    print("string is palindrome")
