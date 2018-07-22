def Calc_Bin(n):
	s=[]
	while(n!=0):
		a=n%2
		s.append(a)
		n=n//2
	return(s[::-1])
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
	nl=Calc_Bin(l[i])
	nl1=[i for i in nl if i==1]
	l1.append(len(nl1))
for i in range(len(l)):
	for j in range(len(l)):
		if(l1[i]>l1[j]):
			l1[j],l1[i]=l1[i],l1[j]
			l[j],l[i]=l[i],l[j]
for i in range(len(l)-1):
	if(l1[i]==l1[i+1]):
		if(l[i+1]>l[i]):
			l[i+1],l[i]=l[i],l[i+1]
	print(l[i])
print(l[len(l)-1])
