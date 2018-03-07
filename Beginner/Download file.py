for _ in range(int(input())):
	n,k=map(int,input().strip().split())
	data=0
	for i in range(n):
		t,d=map(int,input().strip().split())
		if t<=k:
			k=k-t
			t=0
		else:
			t=t-k
			k=0
		data=data+t*d		
	print(data-k)