s=str(input())
l=s.split(" ")
n=int(l[0])
n1=int(l[1])
if(n<n1):
 c=n+1
else:
 c=n1+1
i=1
max=0
while(i!=c):
 if(n%i==0 and n1%i==0):
  max=i
 i+=1
print(max)
