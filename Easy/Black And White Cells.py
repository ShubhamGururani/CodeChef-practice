for _ in range(int(input())):
	ar = list(input())
	if len(ar) % 2 == 1 and ar.index('W') == int(len(ar)/2):
		print ('Chef')
	else:
		print ('Aleksa')