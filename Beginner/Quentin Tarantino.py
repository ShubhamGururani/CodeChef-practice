for _ in range(int(input())):
	n = int(input())
	ar = list(map(int,input().split()))
	s = set(ar)
	m = max(s)
	br = sorted(ar)
	if len(s) < n or n < m or ar == br:
		print("no")
	else:
		print("yes")