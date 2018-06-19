s=str(input())
l=[]
for i in range(len(s)):
 l.append(0)
for i in range(len(s)):
 c=1
 for j in range(len(s)):
  if(i!=j):
   if(s[i]==s[j]):
    l[i]=c
    c+=1
max=l[0]
for i in l:
 if(int(max)<int(i)):
  max=i
c1=0
while(c1!=len(l)-1):
 if(l[c1]==max):
  print(s[c1])
  break
 c1+=1
