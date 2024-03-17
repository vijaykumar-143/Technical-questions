n=input().split()
c="aeiouAEIOU"
v=0
m=""
l=""
print(n)
for i in n:
   print(i)
   m=i
   for j in m:
     if j in c:
       v=v+1
       l=l+j
   print("vowel count",v)
   print("vowels",set(l))
   v=0
   l=""
       
