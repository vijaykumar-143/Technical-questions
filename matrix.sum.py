"""write a python program to print sum of given matrix"""
n,m=map(int,input("enter roew and columns").split())
lst=[]

for i in range(0,n):
    r=[]
    for j in range(0,m):
        r.append(int(input()))
    lst.append(r)
"""
for i in range(n):
  lst.append(list(map(int,input().split())))
"""
#print(lst)  
s=0
for i in lst:
    print(i)
    s=s+sum(i)
print("sum: ",s)


        
