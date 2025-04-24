#4.Write a program code in python to find sum of those item which is (not multiple of 8 and 9) with user input).
sum=0
for i in range(3):
    n=int(input("enter any number"))
    if(n%8!=0 and n%9!=0):
        sum=sum+n
print(sum)
        
