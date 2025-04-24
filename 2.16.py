#16. Write a program code in Python to take a continuous number from user until the user enters a number greater than 300
#and find the sum of all numbers entered by the user

sum = 0
while True:
    num=int(input("enter any number"))
    sum=sum+num
    if(num>300):
        break
print("the sum number enter by user",sum)
    
