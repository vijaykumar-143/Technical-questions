"""write a python program to print the maximum
sum of 2 adjacent values in a matrix"""
n,m=map(int,input("enter roew and columns").split())
lst=[]
for i in range(n):
  lst.append(list(map(int,input().split())))
Max=0
sum=0
for i in lst:
    for j in range(0,len(i)-1):
        sum =(i[j]+i[j+1])
        if sum >= Max:
           Max=sum
print("maximum of 2 adjacent numbers in matrix is :",Max)
   
    
