# Python Program to Remove the nth Index Character from a Non-Empty String

def remove(string,n):
    first=string[:n]
    last=string[n+1:]
    return first+last
string=input("enter the string:")
n=int(input("enter the index of the character to remove:"))
print("modified string:")
print(remove(string,n))
