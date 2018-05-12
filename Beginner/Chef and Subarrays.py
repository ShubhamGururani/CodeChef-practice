for _ in range(int(input())):
	n = int(input())
	ar = [int(i) for i in input().split()]
	count = 0
	for i in range(n):
		su = 0
		prod = 1
		for j in range(i,n):
			su += ar[j]
			prod *= ar[j]
			if su == prod:
				count += 1
	print(count)