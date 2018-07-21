l=input().split()
n=len(l)
c=0
for i in range(0,n):
	j=i
	k=j
	while(j!=n):
			if(l[i]<l[j]<l[k]):
				c+=1
			if(k==n-1):
				k=j
				j+=1
			k+=1
print(c)
