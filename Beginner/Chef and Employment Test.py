for _ in range(int(input())):
	n,k=map(int,input().strip().split())
	ar=list(map(int, input().split()))
	ar.sort()
	print(ar[int((n+k+1)/2)-1])