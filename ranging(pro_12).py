n,q = input().split()
n = int(n)
q = int(q)
array = [int(x) for x in input().split()]
for i in range(q):
	u,v = input().split()
	u = int(u)-1
	v = int(v)-1
	sum = 0
	for i in range(u,v+1):
		sum+=array[i]
	print(sum)
