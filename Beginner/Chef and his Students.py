for _ in range(int(input())):
	a=input().strip()
	count=0
	i=0
	while i<len(a)-2:
		if a[i]+a[i+1]=='<>':
			count+=1
		i+=1
	print(count)