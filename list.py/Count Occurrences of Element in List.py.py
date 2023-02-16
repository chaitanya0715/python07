# Python Program to Count Occurrences of Element in List

n=list(map(int,input("enter ur list:").split()))
k={}
for i in n:
    m = n.count(i)
    k[i] = m 
for i,v in k.items():
    print(i," is repeted in",v,"times")
