for _ in range(int(input())):
	n = int(input())
	ar = list(map(int,input().split()))
	if (sum(ar) - 1) % 2 == 0:
		print("YES")
	else:
		print("NO")