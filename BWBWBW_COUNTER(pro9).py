n=int(input())
b=2*n
l=[]
count,count1=0,0
for i in range(1,b+1):
	if(i<=n):
		l.append('W')
		count+=1
	else:
		l.append('B')
		count1+=1
#print(l)
if(count==count1):
	print((count1+count)//2)
