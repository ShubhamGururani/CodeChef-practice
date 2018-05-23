for _ in range(int(input())):
	num = int(input())
	flag = 0
	for i in range(2, int(num ** 0.5)):
		if num % i == 0:
			flag = 1
			break
	if flag:print("no")
	else:print("yes")