import collections
k=int(input())
a=list(map(int,input().split()))
d=collections.Counter(a)
for x,y in d.items():
    if y==1:
        print(x)

