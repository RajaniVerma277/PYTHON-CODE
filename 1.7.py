#write a program in python to take a number from the user and find whether the remainder is even or odd by dividing 17
num = int(input("enter number from the user"))
remainder = num%17
if(remainder%2 == 0):
    print("remainder is even")
else:
    print("remainder is odd")
