#15. Write a program code in Python to take a string from the user and find the unique character of that string
s = input('enter any string')
non_repe=[]
repe=[]
l=len(s)
i=0
while(i<l):
    if(s[i]>'a' and s[i]<'z' or s[i]>'A' and s[i]<'Z'):
        charc = s[i]
        num = s.count(s[i])
        if(num>1):
            repe.append(s[i])
        else:
            non_repe.append(s[i])
    i+=1
print("non repeating character",non_repe)
print("repeating character",repe)

