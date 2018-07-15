n=int(input())
s=[]
for k in range(n):
 s.append(str(input()))
s1=""
l=len(s[0])
for i in range(0,l):
 f=1
 for j in range(0,n):
  if(s[0][i]==s[j][i]):
   f=1
  else:
   f=0
   break
 if(f==1):
   s1=s1+s[0][i]
 else:
  break
print(s1)
