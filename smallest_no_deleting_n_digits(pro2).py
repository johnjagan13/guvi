from itertools import combinations
s=str(input())
l1=s.split(" ")
length=len(l1[0])-int(l1[1])
l=list(combinations(l1[0],length))
s=[]
for i in range(0,len(l)):
 t=""
 for j in range(0,len(l[i])):
  t=t+l[i][j]
 s.append(int(t))
print(min(s))
