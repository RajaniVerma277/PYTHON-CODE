#2. Write a program code in Python to take a number from user print all even numbers from 1 to that number.
num = int(input("enter any number"))
l = []
i=1
while(i<=num):
    if(i%2==0):
        l.append(i)
    i+=1
print(l)
