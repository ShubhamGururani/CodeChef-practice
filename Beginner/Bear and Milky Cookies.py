for _ in range(int(input())):
	n = int(input())
	ar = input().split()
	f = 0
	x = False
	for i in range(n):
		if ar[i] == "cookie":
			f += 1
		elif ar[i] == "milk":
			if f == 1:
				f -= 1
		if f == 2:
			break
	if f == 0:
		print("YES")
	else:
		print("NO")