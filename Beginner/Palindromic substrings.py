for _ in range(int(input())):
	a = list(input())
	b = list(input())
	if len(set(a).intersection(set(b))) > 0:
		print("Yes")
	else:
		print("No")