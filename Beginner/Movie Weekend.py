for _ in range(int(input())):
	n = int(input())
	l = [int(i) for i in input().split()]
	r = [int(j) for j in input().split()]
	prod = 0
	maxR = 0
	index = 0
	for i in range(n):
		if l[i] * r[i] > prod:
			index = i + 1
			maxR = r[i]
			prod = l[i] * r[i]
		elif l[i] * r[i] == prod and r[i] > maxR:
			index = i + 1
			maxR = r[i]
			prod = l[i] * r[i]
	print(index)