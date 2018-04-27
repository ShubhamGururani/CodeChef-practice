for _ in range(int(input())):
	n = int(input())
	ar = [int(i) for i in input().split()]
	flag = True
	if n % 2 == 0 or ar[0] != 1 or ar[n-1] != 1:
		flag = False
	else:
		for i in range((n)//2):
			if ar[i+1] - ar[i] != 1:
				flag = False
				break
		for i in range((n)//2,n-1):
			if ar[i] - ar[i+1] != 1:
				flag = False
				break
	if flag:
		print("yes")
	else:
		print("no")