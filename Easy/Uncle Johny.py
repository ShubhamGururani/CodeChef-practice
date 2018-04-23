for _ in range(int(input())):
	n = int(input())
	ar = list(map(int,input().split()))
	j = int(input()) - 1
	find = ar[j]
	ar.sort()
	for i in range(len(ar)):
		if ar[i] == find:
			print(i + 1)
			break