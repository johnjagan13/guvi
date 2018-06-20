s=str(input())
f=0
c=0
while(f!=1 and c!=len(s)):
 if(ord(s[c])<48 or ord(s[c])>57):
  f=1
  print("no")
  break
 c+=1
if(f!=1):
 print("yes")
