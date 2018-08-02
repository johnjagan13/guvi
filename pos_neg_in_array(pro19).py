def check(l):
	c=1
	for i in range(len(l)-1):
		if(l[i]>0):
			if(l[i+1]<0):
				c+=1
			else:
				break
		elif(l[i]<0):
			if(l[i+1]>0):
				c+=1
			else:
				break
		else:
			break
	return (c)
n=int(input())
l=[int(i) for i in input().split()]
li=[]
for i in range(n):
	l1=[l[i] for i in range(i,len(l))]
	li.append(check(l1))
s=' '.join(str(i) for i in li)
print(s)
