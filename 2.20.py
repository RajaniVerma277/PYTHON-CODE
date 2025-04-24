#20. Write a program in Python to take a string from the user and find the character which has maximum frequency in the string
s=input("enter any string")
l=len(s)
i=0
maximum=0
while(i<l):
    charc = s[i]
    num = s.count(charc)
    if(num>maximum):
        maximum = num
        max_char = s[i]
    i+=1
print("max frequency",maximum)
print("maximum character",max_char)
