N,A,B=input().split()
sum=0
f=0
while(True):
 sum+=int(A)+int(B)
 if int(N)==sum:
   print("YES")
   break
 if sum>int(N):
  f=1
  break
if(f==1):
 print("NO")
