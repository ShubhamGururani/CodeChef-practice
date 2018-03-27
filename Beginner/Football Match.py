for _ in range(int(input())):
	count1 = 0
	count2 = 0
	team1 = ""
	team2 = ""
	for _ in range(int(input())):
		s = input()
		if team1 == "" or team1 == s:
			team1 = s
			count1 += 1
		else:
			team2 = s
			count2 +=1
	if count1 > count2:
		print(team1)
	elif count2 > count1:
		print(team2)
	else:
		print("Draw")