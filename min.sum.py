"""write a python program to print minimum
sum of 2 adjacent values in a list and also print indexes"""
lst=list(map(int,input("enter the list").split()))
min=lst[0]+lst[1]
a,b,sum=0,0,0
for i in range(0,(len(lst)-1)):
    sum=lst[i]+lst[i+1]
    if sum<=min:
        a=i;b=i+1;min=sum
print("indexes are",a,"and",b ,"minimum sum is:",min)
        
        
    
    
    
