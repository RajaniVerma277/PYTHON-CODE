#18. Write a program in Python to take a continuous number from the user until the user enters five odd numbers and
#finds the sum of all even numbers entered by the user
count=0
sum=0
while True:
    num = int(input("enter any number"))
    if(num%2==0):
        sum=sum+num
    if(num%2!=0):
        count+=1
        if(count>4):
            break
print("the sum of all number",sum)
