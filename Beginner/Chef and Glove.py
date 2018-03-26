for _ in range(int(input())):
	n = int(input())
	finger = list(map(int,input().split()))
	glove = list(map(int,input().split()))
	notOkFront = 0
	notOkBack = 0
	for i in range(n):
		if finger[i] > glove[i]:
			notOkFront += 1
		if finger[i] > glove[n - i - 1]:
			notOkBack += 1
	if notOkFront == 0 and notOkBack == 0:
		print("both")
	elif notOkFront == 0:
		print("front")
	elif notOkBack == 0:
		print("back")
	else:
		print("none")