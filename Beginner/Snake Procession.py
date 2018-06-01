for _ in range(int(input())):
	num = int(input())
	s = input()
	valid = 0
	flg = 0
	for char in s:
		if valid > 1 or valid < 0:
			flg = 1
			break
		if char == "H":
			valid += 1
		elif char == "T":
			valid -= 1
	if flg == 0 and valid == 0:
		print("Valid")
	else:
		print("Invalid")