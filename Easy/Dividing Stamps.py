n = int(input())
ar = list(map(int,input().split()))
if sum(ar) == n * (n + 1) / 2:print('YES')
else:print('NO')