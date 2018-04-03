for _ in range(int(input())):
	x, y = map(int,input().split())
	num = x + y + 1
	z = int(num/2) + 1
	while True:
		if num % z == 0:
			num += 1
			z = int(num/2) + 1
		else:
			z -= 1
		if z < 2:
			print(num - x - y)
			break