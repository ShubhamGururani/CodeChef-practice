for i in range(int(input())):
    n,m = map(int,input().split())
    n=int(n)
    m=int(m)
    room=list(map(int,input().strip().split()))
    r=[0]*n
    for j in room:
        r[j]+=1
    count=0
    for k in range(0,n):
        b=list(map(int,input().strip().split()))[1:]
        b.sort(reverse=True)
        count+=sum(b[:r[k]])
    print(count)