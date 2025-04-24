#23. Write a program code in Python to take a continuous name from the user until the user enters 10 names
#with even length and returns all 10 names in a list.
name=[]
count=0
while True:
    s=input("enter name")
    l=len(s)
    if(l%2==0):
        name.append(s)
    count+=1   
    if(count>10):
        break
print(name)

