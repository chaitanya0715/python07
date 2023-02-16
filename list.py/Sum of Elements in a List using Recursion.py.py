# Python Program to Find the Sum of Elements in a List using Recursion

def summrize(n,l):
    if l ==0:
        return 0
    else:
        return n[l-1]+summrize(n,l-1)
n=list(map(int,input("enter ur list:").split()))
l = len(n)
b = summrize(n,l)
print(b)
