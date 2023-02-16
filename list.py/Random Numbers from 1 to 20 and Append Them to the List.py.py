# Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
import random
a=[]
n=int(input("enter the number of elements: "))
for j in range(n):
    a.append(random.randint(1,20))
print('randomised list is:',a)
