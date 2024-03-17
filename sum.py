""" write a python program to print
sum of elenments in a list with in a range"""
lst=list(map(int,input("enter the list").split()))
print(sum(lst[:int(input())]))
"""n=int(input("enter the range"))
sum=0
for i in range(0,len(lst)):
    if(i==(n+1)):
        break
    else:
        sum=sum+lst[i]
print(sum)"""
