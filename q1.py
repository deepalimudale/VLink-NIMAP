n = int(input())
l=[]
li=[]
if n>0:
    for i in range(n):
        c = input()
        l.append(c)
        li.append(len(c))
else:
    print("invalid output")
l.sort()
print(l)
ma = max(li)
res=li.index(ma)
print(l[res])
