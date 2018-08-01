from itertools import combinations
m,n=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
#print(l)
li=list(combinations(l,2))
flag=0
for i in li:
	s=list(i)
	if(sum(s)==n):
		print("yes")
		flag=1
		break
if(flag==0):
	print("no")
