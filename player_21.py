l3=[]
for i in range(3):
 s=str(input())
 l3.append(s)
l=l3[0].split(" ")
l1=l3[1].split(" ")
l2=l3[2].split(" ")
if(l[0]==l1[0] and l2[0]==l1[0] and l[0]==l2[0]):
 print("yes")
elif(l[1]==l1[1] and l2[1]==l1[1] and l[1]==l2[1] ):
 print("yes")
else:
 print("no")
