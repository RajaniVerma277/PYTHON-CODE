#write a program in python to take number from the user and check whether the number is divisible by 4 and 8 or not
num = int(input("enter number from the user"))
if(num%4==0 and num%8==0):
    print("number is divisible by 4 and 8")
else:
    print("number is not divisible by 4 and 8")
