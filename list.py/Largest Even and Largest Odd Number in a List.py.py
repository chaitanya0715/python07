# Python Program to Print Largest Even and Largest Odd Number in a List
a=[2,3,4,5,6,7,8,9]
odd =[]
even =[]

for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print("enter the element")
