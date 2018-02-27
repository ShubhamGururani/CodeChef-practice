t=int(input())
while t>0:
    notFound=True
    A,B=map(int,input().strip().split())
    l=0
    b=0
    i=1
    while(notFound):
        l=l+i
        i=i+1
        if l>A:
            notFound=False
            print('Bob')
            break
        b=b+i
        i=i+1
        if b>B:
            notFound=False
            print('Limak')
            break
    t=t-1