#check string is palindrome or not
string = input("enter any string")
if(string == string[::-1]):
    print("string is palindrome")
else:
    print("string is not palindrome")
