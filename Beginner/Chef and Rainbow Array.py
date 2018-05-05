rainbow = {1,2,3,4,5,6,7}
for _ in range(int(input())):
	n = int(input())
	ar = [int(i) for i in input().split()]
	i = 0
	j = n - 1
	flag = False
	while i < j:
		if ar[i] != ar[j]:
			flag = True
			break
		i += 1
		j -= 1
	if set(ar) != rainbow:
		flag = True
	if flag:
		print("no")
	else:
		print("yes")