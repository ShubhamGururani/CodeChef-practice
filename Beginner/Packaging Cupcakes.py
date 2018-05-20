for _ in range(int(input())):
	num = int(input())
	if num % 2 == 0:
		print(num // 2 + 1)
	else:
		print((num + 1) // 2)