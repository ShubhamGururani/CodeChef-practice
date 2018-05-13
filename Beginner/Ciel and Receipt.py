for _ in range(int(input())):
	n = int(input())
	num = 0
	j = 11
	while j >= 0:
		x = 2 ** j
		if x <= n:
			n -= x
			num += 1
			continue
		elif n == 0:
			break
		else:
			j -= 1
	print(num)