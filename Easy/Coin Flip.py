for _ in range(int(input())):
	for _ in range(int(input())):
		i,n,q = map(int,input().split())
		if n % 2 != 0:
			same = int(n/2)+1
			diff = n - same
		else:
			same = diff = int(n/2)
		if q == i:
			print(diff)
		else:
			print(same)