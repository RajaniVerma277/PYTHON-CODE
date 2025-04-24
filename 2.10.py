#10. Write a program in Python to take a number from the user and check whether the number is armstrong or not
num = int(input("enter any number"))
num1=num
temp = num1
count=0
sum=0
while(num>0):
    count+=1
    num=num//10
    
while(num1>0):
    rem=num1%10
    sum=sum+pow(rem,count)
    num1=num1//10
print(sum)
if(temp==sum):
    print("number is armstrong")
else:
    print("number is not armstrong")

