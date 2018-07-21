def GCD(n1,n2):
	i=1
	while(i%n1!=0 or i%n2!=0):
		i+=1
	return((n1*n2)//i)
n,m=input().split()
l=input().split()
for i in range(int(m)):
	p,q=input().split()
	result=GCD(int(l[int(p)-1]),int(l[int(q)-1]))
	print(result)
