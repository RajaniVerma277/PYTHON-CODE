#7. Write a program code in Python to take a number from the user and find the factorial of that number
num = int(input("enter any number to find factorial"))
fact = 1
while(num>0):
    fact=fact*num
    num-=1
print(fact)

