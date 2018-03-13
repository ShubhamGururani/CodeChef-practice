for _ in range(int(input())):
	a=input()
	b=input()
	a=a.strip().split()
	b=b.strip().split()
	count=0
	flag=0
	for item in a:
		if item in b:
			count+=1
		if count>=len(a)/2:
			flag=1
			print("similar")
			break
	if flag==0:
		print("dissimilar")		