for _ in range(int(input())):
	a=input().strip()
	i=len(a)-1
	sum=0
	while i>=0:
		sum+=int(a[i])
		i-=1
	print(sum)	