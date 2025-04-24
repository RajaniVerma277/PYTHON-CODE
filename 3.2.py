#2.Write a program code in python to find the sum of those item having even index in the list.
l=[10,20,30,40,50,60]
sum=0
for i in range(0,len(l)):
    if(i%2==0):
        sum=sum+l[i]
print("the total sum of even index number is=",sum)
