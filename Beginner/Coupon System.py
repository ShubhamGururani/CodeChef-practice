for _ in range(int(input())):
	n = int(input())
	a = []
	val = []
	for _ in range(n):
		s = [int(i) for i in input().split(" ")]
		val.append(s[1])
		a.append(s)
	val = set(val)
	for item in val:
		maxDisc = False
		maxDiscCity = False
		for i in range(n):
			disc = a[i][2]
			city = a[i][0]
			if item == a[i][1]:
				if disc > maxDisc or maxDisc == False:
					maxDisc = disc
					maxDiscCity = city
				elif disc == maxDisc:
					if city < maxDiscCity:
						maxDiscCity = city
		print(maxDisc, maxDiscCity)