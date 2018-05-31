for _ in range(int(input())):
	n = input()
	n1 = ""
	for i in range(len(n) - 1, -1, -1):
		n1 += n[i]
	print(int(n1))