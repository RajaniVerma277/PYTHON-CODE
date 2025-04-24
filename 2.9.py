#9. Write a program in Python to take a number from the user and print the reverse of that number
num = int(input("enter any number"))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
