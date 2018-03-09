for _ in range(int(input())):
	n=int(input().strip())
	i=0
	a=input().strip().split()
	b=input().strip().split()
	for i in range(len(a)):
		a[i]=int(a[i])
		b[i]=int(b[i])
	i=len(a)-1
	while i>0:
		a[i]-=a[i-1]
		i-=1	
	count=0
	i=0
	for i in range(len(a)):
		if a[i]>=b[i]:
			count+=1
	print(count)