for _ in range(int(input())):
	s = input()
	b = []
	b.extend(s)
	a = sorted(b)
	if a != b:
		print("no")
	else:
		print("yes")