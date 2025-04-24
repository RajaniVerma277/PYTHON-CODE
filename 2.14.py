#14. Write a program code in Python to take a string from the user and find how many duplicates are present in the string
s = input("enter any string")
non_repe = set()
repe= set()
l= len(s)
i=0
while(i<l):
    charc = s[i]
    num = s.count(charc)
    if(num>1):
        repe.add(s[i])
    else:
        non_repe.add(s[i])
    i+=1
print("repeating character are",repe)
