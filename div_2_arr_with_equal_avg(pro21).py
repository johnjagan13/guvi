from itertools import permutations,combinations
def find_avg(arr,size):
	sum=0
	for i in range(size):
		sum+=arr[i]
	return(sum//size)
n=int(input())
l=[int(i) for i in input().split()]
avg=[]
f=0
for i in range(1,len(l)):
	li=list(combinations(l,i))
	for j in li:
		lis=list(j)
		sum=find_avg(lis,len(lis))
		if sum not in avg:
			avg.append(sum)
		else:
			f=1
if(f==1):
	print("yes")
else:
	print("no")
#print(find_avg(l,len(l)))
#print(list[combinations(l,3)))
