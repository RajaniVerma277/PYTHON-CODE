#12. Write a program code in Python to take a string from the user and find the second non repeating character of the string
s = input("enter any string")
non_repe = []
repe= []
i=len(s)
print(i)
j=0

while(j<i):
    char = s[j]
    num = s.count(char)
    print(num)
    if(num>1):
        repe.append(s[j])
    else:
        non_repe.append(s[j])
        
    j+=1

print("non repeating character",non_repe)
print("repeating character",repe)
print("second non repeating character",non_repe[1])

