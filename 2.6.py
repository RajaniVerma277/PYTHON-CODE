#6. Write a program code in Python to take a number from the user and find the multiplication of the digit of that number.
num = int(input("enter number from user"))
pro = 1
while(num>0):
    rem = num%10
    pro*=rem
    num=num//10
print(pro)

