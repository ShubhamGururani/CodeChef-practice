t=int(input())
while t>0:
	x1,y1,x2,y2=map(int,input().split())
	if  y1==y2 and x1<x2:
		print('right')
	elif y1==y2 and x1>x2 :
		print('left')
	elif y1<y2 and x1==x2:
		print('up')
	elif y1>y2 and x1==x2:
	    print('down')
	else:
		print('sad')    			
	t=t-1