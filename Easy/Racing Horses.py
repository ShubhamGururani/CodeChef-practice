for _ in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	minDiff = None
	diff = 0
	for i in range(n - 1):
		diff = a[i+1] - a[i]
		if minDiff is None or minDiff > diff:
			minDiff = diff
	print(minDiff)