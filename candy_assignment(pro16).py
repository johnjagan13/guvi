n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
	l1.append(1)
for i in range(1,len(l)):
	if(l[i]>l[i-1]):
		while(l1[i]<=l1[i-1]):
			l1[i]+=1
sum=0
for i in l1:
	sum+=i
print(sum)
