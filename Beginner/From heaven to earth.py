for _ in range(int(input())):
	n,v1,v2=map(int,input().strip().split())
	eleTime=2*n/v2
	perTime=(2**0.5)*n/v1
	if eleTime<perTime:
		print("Elevator")
	else:
		print("Stairs")