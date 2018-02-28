t=int(input())
while t>0:
	s=input()
	i=0
	c1=0
	c2=0
	while i<len(s)-1:
		if s[i]=='D' and s[i+1]=='U':
			c1=c1+1
		if s[i]=='U' and s[i+1]=='D':
			c2=c2+1	
		i=i+1
	print(max(c1,c2))		
	t=t-1