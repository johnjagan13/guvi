n=int(input())
l=[]
c=0
for i in range(2,n+1):
 f=0
 for j in range(1,n+1):
  if(i%j==0):
   f=f+1
 if(f==2):
  l.append(i)
l1=[i for i in l if n%i==0]
s=""
if(len(l1)>0):
 for i in l1:
  s=s+str(i)
  if(c!=len(l1)-1):
   s=s+" "
  c+=1
 print(s)
else:
 print(0)
