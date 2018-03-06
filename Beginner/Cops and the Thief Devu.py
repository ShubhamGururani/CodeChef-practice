for _ in range(int(input())):
	M,x,y=map(int,input().split())
	z=x*y
	count=0
	l=list(map(int,(input().split())))
	for i in range(1,101):
		flag=0
		for item in l:
			if i in range(item-z,item+z+1):
				flag=1
				break
		if flag==0:
			count+=1
	print(count)			


