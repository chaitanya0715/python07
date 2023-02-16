#Python Program to Find the Number Occurring Odd Number of Times in a List

def find_odd_occuring(alist):
    ans=0
    for element in alist:
        ans^=element
    return ans

alist=input("enter the list:").split()
alist=[int(i) for i in alist]
ans=find_odd_occuring(alist)
print("the element that occurs odd number of times:",ans)
