for _ in range(int(input())):
	n = int(input())
	s = input()
	flag = 0
	for char in s:
		if char == "I":
			flag = 1
			break
		if char == "Y":
			flag = 0
			break
		else:
			flag = 2
	if flag == 0:
		print("NOT INDIAN")
	elif flag == 1:
		print("INDIAN")
	else:
		print("NOT SURE")