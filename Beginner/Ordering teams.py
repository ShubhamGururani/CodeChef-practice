def check(a,b):
	flag=False
	for i in range(3):
		if b[i]>a[i]:
			flag=True
		elif b[i]<a[i]:
			return False
	return flag

for _ in range(int(input())):
	a=list(map(int,input().strip().split()))
	b=list(map(int,input().strip().split()))
	c=list(map(int,input().strip().split()))
	if (check(a,b) and check(b,c)) or (check(a,c) and check(c,b)) or (check(b,a) and check(a,c)) or (check(b,c) and check(c,a)) or (check(c,a) and check(a,b)) or (check(c,b) and check(b,a)):
		print("yes")
	else:
		print("no")