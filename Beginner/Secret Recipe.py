for _ in range(int(input())):
	ar = [int(i) for i in input().split()]
	dist1 = ar[2] - ar[0]
	dist2 = ar[1] - ar[2]
	if dist1/ar[3] >dist2/ar[4]:
		print("Kefa")
	elif dist1/ar[3] < dist2/ar[4]:
		print("Chef")
	else:
		print("Draw")