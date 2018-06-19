k=int(input())
s=str(input())
l=s.split(" ")
n=len(l)
l1=[]
for i in range(n):
 l1.append(5555)
for i in range(n):
 for j in range(n):
  if(i!=j):
   if(l[i]==l[j]):
    l1[i]=0
for i in range(n):
 if l1[i]>0:
  print(l[i])
