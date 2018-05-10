for i in range(int(input())):
	base = int(input())
	sq = 0
	if base % 2 == 0:
		half = base//2
		sq = (half**2-half)//2
	else:
		half = (base-1)//2
		sq = (half**2-half)//2
	print(sq)