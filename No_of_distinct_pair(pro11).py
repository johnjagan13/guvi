n=int(input())
c=0
for i in range(1,n+1):
	for j in range(i+1,n+1):
		c+=1
if(c%(n-1)==0):
	print(c)
else:
	print(c-(c%(n-1)))
