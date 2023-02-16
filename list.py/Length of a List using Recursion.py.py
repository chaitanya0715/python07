# Python Program to Find the Length of a List using Recursion

def len_list(n):
    if n == 0:
        return 0
    return 1 + len_list(n[1:])
n=list(map(int,input("enter ur list:").split()))
k = len_list(n)
print("length is:",k)
