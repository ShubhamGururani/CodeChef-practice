for _ in range(int(input())):
    n,r = map(int,input().split())
    ar = list(map(int, input().split()))
    big = max(ar) + 1
    small = 0
    c = 0
    if r != ar[len(ar) - 1]:
        print('NO')
    for i in range(n-1):
        if small >= big or ar[i] > big or ar[i] < small:
            c = 1
            print('NO')
            break
        if ar[i+1] < ar[i]:
            big = ar[i]
        else:
            small = ar[i]
    if c == 0 and r < big and r > small:
        print('YES')
    elif c == 0:
        print('NO')