for _ in range(int(input())):
	n = int(input())
	ar = list(map(int,input().split()))
	ar.sort(reverse = True)
	Amount = 0
	count = 0
	for i in range(n):
		if count < 2:
			Amount += ar[i]
		elif count == 3:
			count = 0
			continue
		count += 1
	print(Amount)