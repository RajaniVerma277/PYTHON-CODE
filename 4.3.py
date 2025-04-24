"""   *
     ***
    *****
   *******
  *********    """
n=int(input("enter number to print star"))
for i in range(1,n+1):
    print(((n-i)*" ")+(i*"*")+((i-1)*"*"))
