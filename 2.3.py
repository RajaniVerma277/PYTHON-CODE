#3. Write a program code in Python to take a number from the user and print a reminder of all numbers divided by 8 from 1 to
#that number.
num = int(input("enter any number"))
l=[]
i=1
while(i<=num):
    rem = i%8
    l.append(rem)
    i+=1
print(l)
