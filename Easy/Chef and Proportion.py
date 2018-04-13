ar = list(map(int,input().split()))
ar.sort()
if ar[1] / ar[0] == ar[3] / ar[2] or ar[2] / ar[0] == ar[3] / ar[1]:
	print("Possible")
else:
	print("Impossible")