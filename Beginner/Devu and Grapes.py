for _ in range(int(input())):
    a, b = map(int,input().split())
    ar = [int(i) for i in input().split()]
    ans = 0
    for i in range(a):
        if ar[i] > b:
            ans += min(ar[i] % b, b - ar[i] % b)
        elif ar[i] < b:
            ans += b - ar[i] % b 
    print(ans)
