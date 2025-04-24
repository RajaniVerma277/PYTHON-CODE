#write a program in python to take 4 digit number and repalce first and last number
num = input("enter four digit number")
new_num = num[-1]+num[1:3]+num[0]
print("the new number is",new_num)
