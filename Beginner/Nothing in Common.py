for _ in range(int(input())):
	n, m = map(int,input().split())
	Alice = set(map(int,input().split()))
	Berta = set(map(int,input().split()))
	print(len(Alice.intersection(Berta)))