t=int(input())
while t>0:
	s=input()
	c=s.count('1')
	if c==0:
		print("Beginner")
	elif c==1:
		print("Junior Developer")
	elif c==2:
		print("Middle Developer")
	elif c==3:
		print("Senior Developer")
	elif c==4:
		print("Hacker")
	elif c==5:
		print("Jeff Dean")	
	t=t-1