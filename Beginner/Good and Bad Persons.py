for _ in range(int(input())):
	n,k=map(int,input().split())
	s=input()
	small=0
	caps=0
	for char in s:
		if char.isupper():
			caps+=1
		if char.islower():
			small+=1
	if small<=k and caps<=k:
		print("both")
	elif caps<=k:
		print("chef")
	elif small<=k:
		print("brother")
	else:
		print("none")