#17. Write program code in Python to take a continuous number from the user until the user enters a negative number  and
#returns all numbers entered by the user in a list
l=[]
while True:
    num = int(input("enter any number"))
    l.append(num)
    if(num<0):
        break
print(l)
