for _ in range(int(input())):
	a=input()
	b=input()
	qAny=0
	qOne=0
	for i in range(len(a)):
		if(a[i]==b[i] and a[i]=='?'):
			qAny=qAny+1
		elif(a[i]!=b[i] and (a[i]=='?'or b[i]=='?')):
			qAny=qAny+1
		elif(a[i]!=b[i]):
			qOne=qOne+1
	print(qOne,qOne+qAny)		
