for _ in range(int(input())):
	lost=0
	for _ in range(int(input())):
		p,q,d=map(int,input().strip().split())
		inc=p*d/100
		bacha=p+inc
		disc=bacha*d/100
		x=bacha-disc
		lost+=q*(p-x)
	print(lost)