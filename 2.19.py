#19. Write a program code in Python to take a string from the user and find a second last non repeating character from the string
s=input("enter any string")
l=len(s)
non_repe=[]
repe=[]
i=0
while(i<l):
    charc=s[i]
    num = s.count(s[i])
    if(num>1):
        repe.append(s[i])
    else:
        non_repe.append(s[i])
    i+=1
print("second last non repeating character",non_repe[-2])
