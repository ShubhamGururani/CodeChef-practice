for _ in range(int(input())):
	x = list(map(int,input().split()))
	continuous = 0
	flag = 0
	i = 0
	while i < len(x):
		if x[i] == 1:
			continuous += 1
			if continuous > 5:
				print("#coderlifematters")
				flag = 1
				break
		elif x[i] == 0:
			continuous = 0
		i += 1	
	if flag == 0:
		print("#allcodersarefun")