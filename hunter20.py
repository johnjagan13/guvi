def Calc_Bin(n):
	s=[]
	while(n!=0):
		a=n%2
		s.append(a)
		n=n//2
	print(s[::-1])
	return(s[::-1])
def prime(n):
	for i in range(2,n//2):
		if(n%i==0):
			return(False)
	return(True)
l=list(map(int,input().split()))
l1=[]
sum=0
for i in range(len(l)):
	nl=Calc_Bin(l[i])
	nl1=[i for i in nl if i==1]
	print(len(nl1))
	if(len(nl1)>1):
		if(prime(len(nl1))):
			sum+=len(nl1)
	else:
		sum+=len(nl1)
print(sum)
