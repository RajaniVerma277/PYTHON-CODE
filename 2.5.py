#5. Write a program code in Python to take a number from the user and find the sum of digits of that number.
num = int(input("enter number from user"))
sum = 0
while(num>0):
    rem = num%10
    sum+=rem
    num=num//10
print(sum)
