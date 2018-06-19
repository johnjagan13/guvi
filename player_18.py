try:
    n = int(input())
    s=[0]*n
    c =dict()
    b = dict()
    count=0
    g="kabali"
    for i in range(len(g)):
        c.setdefault(g[i],0)
        c[g[i]]+=1
    print(c)
    for i in range(n):
        s[i] = input()
        a = s[i]
        if(len(a)==len(g)):
            for j in range(len(a)):
                b.setdefault(a[j],0)
                b[a[j]]+=1
        if(b==c):
            count+=1
        b.clear()    
    print(count)
except:
    print("Invalid Input")
