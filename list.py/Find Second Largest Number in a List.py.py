# Python Program to Find Second Largest Number in a List


m= list(map(int,input("enter your list:").split()))
x=sorted(m)
print(x[len(x)-2])
