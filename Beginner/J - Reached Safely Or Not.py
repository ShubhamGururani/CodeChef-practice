for i in range(int(input())):
	M,N=map(int,input().split())
	Rx,Ry=map(int,input().split())
	x=0
	y=0
	z=int(input())
	s=input()
	for char in s:
		if char=='L':
			x-=1
		elif char=='R':
			x+=1
		elif char=='U':
			y+=1
		elif char=='D':
			y-=1
	if x<0 or x>M or y<0 or y>N:
		print("Case %d: DANGER"%(i+1))
	elif x==Rx and y==Ry:
		print("Case %d: REACHED"%(i+1))
	else:
		print("Case %d: SOMEWHERE"%(i+1))