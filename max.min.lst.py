""" write a python program to print maximum and minimum in list
of non repeating elelemts in a given list """
lst=[]
for i in range(0,6):
    a=int(input())
    lst.append(a)
for i in lst:
    l=lst.count(i)
    if(l>1):
      for j in lst:
         if j==i:
           lst.remove(j)
print("maximum is :",max(lst))
print("minimum is :",min(lst))
print(len(lst))










    
