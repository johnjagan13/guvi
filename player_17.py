s=str(input())
l=s.split(" ")
n=int(l[0])
n1=int(l[1])
f=0
c=1
while(f!=1):
 if(c%n==0 and c%n1==0):
  print(c)
  f=1
 else:
  c+=1
 
