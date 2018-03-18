for _ in range(int(input())):
	n=int(input())
	x=map(int,input().strip().split())
	fine=0
	before0=0
	due=0
	for item in x:
		if item == 0:
			fine+=1
			before0+=1
			due+=1
		if item == 1:
			if before0>0:
				fine+=1
	print(due*1000+fine*100)