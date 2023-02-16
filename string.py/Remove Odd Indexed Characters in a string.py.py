# Python Program to Remove Odd Indexed Characters in a string

str1=input("enter the string:")
r_str=""
for i in range(len(str1)):
    if(i%2==0):
        r_str+=str1[i]
print(r_str)

