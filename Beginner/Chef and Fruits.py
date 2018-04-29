for _ in range(int(input())):
	n, m, k = map(int,input().split())
	maxC = max(n,m)
	minC = min(n,m)
	diff = maxC - min(minC+k,maxC)
	print(diff)