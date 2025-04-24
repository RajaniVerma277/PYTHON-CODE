a=0
l=[]
while(a<=5):
    k=int(input("enter any number"))
    k1=k
    while(k1>0):
        if((k1%10)%2==0):
            l.append(k)
            a+=1
            break
        else:
            k1=k1//10
print(l)
