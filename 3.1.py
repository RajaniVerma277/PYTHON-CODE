#1.Write a program code in python to find the character with maximum frequency ... (With user input).
n=input("enter any string")
maximum=0
for i in n:
    if(i>'a' or i<'z'  and i>'A' or i<'Z'):
        if(n.count(i)>maximum):
            maximum=n.count(i)
            letter=i

print("the maximumu frequency letter",letter)
print("the maximum frequency is",maximum)
        
