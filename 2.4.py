#4. Write a program code in Python to take a number from the user and find how many digits are present in that number.
num = int(input("enter any number"))
count=0
while(num>0):
    count+=1
    num = num//10
print(count)
