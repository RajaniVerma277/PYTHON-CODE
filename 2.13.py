#13. Write a program code in Python to take a string from the user and find how many characters are present in the string
s = input("enter any string")
charc = []
l = len(s)
i=0
while(i<l):
    if(s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z'):
        charc.append(s[i])
    i+=1
print(len(charc))
