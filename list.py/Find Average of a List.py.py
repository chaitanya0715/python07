# Python Program to Find Average of a List
def is_avg(n):
    
    l = int(len(n))
    total = 0
    for i in n:
        total= total +i
        avg = total/l
    return total, avg
n=[1,2,3,4]                 #list(map(int,(input("enter ur list:").split())))
print(is_avg(n))
