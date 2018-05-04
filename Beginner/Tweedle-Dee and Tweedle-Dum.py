for _ in range(int(input())):
	n,p = input().split()
	n = int(n)
	ar = [int(x) for x in input().split()]
	if n == 1 and ar[0] % 2 == 0 and p =='Dee':
		print("Dee")
	else:
		print("Dum")