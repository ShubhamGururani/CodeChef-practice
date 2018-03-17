for _ in range(int(input())):
	s=input()
	i=0
	count=0
	fin=set('chef')
	while i<=len(s)-4:
		sub=set(s[i:i+4])
		if fin==sub:
			count+=1
		i+=1	
	if count==0:
		print("normal")
	else:
		print("lovely",count)