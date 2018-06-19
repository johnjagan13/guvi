s=str(input())
s1=""
for i in range(len(s)):
 if(ord(s[i])>87):
  if(ord(s[i])==88):
   s1=s1+"A"
  if(ord(s[i])==89):
   s1=s1+"B"
  if(ord(s[i])==90):
   s1=s1+"C"
 else:
  s1=s1+chr(ord(s[i]) + 3)
print(s1)
