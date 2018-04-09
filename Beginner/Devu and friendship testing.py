for _ in range(int(input())):
	friends = int(input())
	ar = list(map(int,input().split()))
	ar = set(ar)
	print(len(ar))