# Python Program to Split Even and Odd Elements into Two Lists
numbers =[]
n = int(input("enter number of elements: \t"))

for i in range(1, 1+n):
    allElements = int(input("enter element: \t"))
    numbers.append(allElements)


even_lst = []
odd_lst = []

for j in numbers:
    if j % 2 == 0:
        even_lst.append(j)
    else:
        odd_lst.append(j)
print("Even numbers list \t", even_lst)
print("odd numbers list \t", odd_lst)
