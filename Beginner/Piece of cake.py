for _ in range(int(input())):
	x=input().strip()
	m=max(x,key=x.count)
	maxcount=0
	other=0
	for char in x:
		if char==m:
			maxcount+=1
		else:
			other+=1		
	if maxcount==other:
		print("YES")
	else:
		print("NO")