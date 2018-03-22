for _ in range(int(input())):
    n,m=map(int,input().strip().split())
    x=n*m
    if x%2==0:
        print("Yes")
    else:
        print("No")