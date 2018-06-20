s=str(input())
s1=""
for i in range(len(s)):
 if(ord(s[i])>=97 and ord(s[i])<=122):
  s1=s1+s[i].upper()
 elif(ord(s[i])>=65 and ord(s[i])<=90):
  s1=s1+s[i].lower()
print(s1)
