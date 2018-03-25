for _ in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	a.sort()
	b.sort()
	sumA = sum(a) - a[len(a) - 1]
	sumB = sum(b) - b[len(b) - 1]
	if sumA < sumB:
		print("Alice")
	elif sumB < sumA:
		print("Bob")
	else:
		print("Draw")