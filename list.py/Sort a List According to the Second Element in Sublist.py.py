# Python Program to Sort a List According to the Second Element in Sublist

a=[['A',25],['B',18],['c',45]]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j][1]>a[j+1][1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)

