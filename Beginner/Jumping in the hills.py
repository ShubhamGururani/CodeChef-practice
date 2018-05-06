for _ in range(int(input())):
	n,u,d = map(int,input().split())
	ar = [int(i) for i in input().split()]
	prev = ar[0]
	para = False
	num = 1
	for i in range(1,n):
		current = ar[i]
		if current > prev:
			if current - prev <= u:
				num += 1
				prev = current
			else:
				break
		elif current == prev:
			prev = current
			num += 1
		else:
			if prev - current <= d:
				num += 1
				prev = current
			elif para == False:
				num += 1
				para = True
				prev = current
			else:
				break
	print(num)