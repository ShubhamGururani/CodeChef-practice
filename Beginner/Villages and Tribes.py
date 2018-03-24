for _ in range(int(input())):
	s = input()
	i = 0
	dot = 0
	a = 0
	b = 0
	prev = '0'
	while i < len(s):
		if prev == 'A' and s[i] == 'A':
			a += dot
			a += 1
			dot = 0
		elif prev == 'B' and s[i] == 'B':
			b += dot
			dot = 0
			b += 1
		elif s[i] == '.':
			dot += 1
		elif s[i] == 'A':
			a += 1
			prev = 'A'
			dot = 0
		elif s[i] == 'B':
			b += 1
			prev = 'B'
			dot = 0
		i += 1
	print(a,b)