t=int(input())
while t>0:
	money=0
	a = [int(x) for x in input().split()]
	s=input()
	chars='abcdefghijklmnopqrstuvwxyz'
	i=0
	while i<26:
		if chars[i] not in s:
			money=money+a[i]
		i=i+1
	print(money)	
	t=t-1