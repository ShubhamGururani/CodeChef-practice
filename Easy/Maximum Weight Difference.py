for _ in range(int(input())):
	n , k = map(int,input().split())
	ar = list(map(int,input().split()))
	ar.sort()
	if k > n - k:
		k = n - k
	father = sum(ar[k:])
	son = sum(ar[:k])
	print(father-son)