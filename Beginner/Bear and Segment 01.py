t=int(input())
while t>0:
    s=input().strip("0")
    a=[int(x) for x in s]
    if a==[]:
        print("NO")
    elif sum(a)==len(a):
        print("YES")
    else:
        print("NO")
    t=t-1