for _ in range(int(input())):
	w,s=input().strip().split()
	w=int(w)
	ar=[0,0,0,0,0,0,0]
	i=1
	while i<=w:
		ar[i%7]+=1
		i+=1
	if s=='mon':
		print(*ar[1:7],ar[0])
	elif s=='tues':
		print(*ar)
	elif s=='wed':
		print(*ar[6:7],*ar[0:6])
	elif s=='thurs':
		print(*ar[5:7],*ar[0:5])
	elif s=='fri':
		print(*ar[4:7],*ar[0:4])
	elif s=='sat':
		print(*ar[3:7],*ar[0:3])
	else:
		print(*ar[2:7],*ar[0:2])