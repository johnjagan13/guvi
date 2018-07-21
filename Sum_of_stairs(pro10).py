n=int(input())
l=input().split()
sum=0
for i in l:
	a=0
	n=int(i)
	for j in range(1,n):
		a+=j
	sum=sum+a
print(sum)
