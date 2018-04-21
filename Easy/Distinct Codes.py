for _ in range(int(input())):
	s = input()
	ar = [] 
	i = 0
	while i < len(s)-1:
		sub = s[i:i+2]
		if sub not in ar:
			ar.append(sub)
		i += 1
	print(len(ar))