l1=[1,10,9,4,0,5]
k=[0,0,0,0,0,0]
s='juk'
l=[]
c=50
n=len(l1)
l1.sort(reverse=True)
while(c!=0):
	if(n!=0):
		for i in range(0,n):
			k[i]=k[i]+1
			c=c-1
		n=n-1
	else:
		n=len(l1)
		for i in range(0,n):
			if(c!=0):
				k[i]=k[i]+1
				c=c-1
			else:
				break
		break
print k
