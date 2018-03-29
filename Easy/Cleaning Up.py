for _ in range(int(input())):
	n,m = map(int,input().split())
	completed = list(map(int,input().split()))
	chef = []
	assistant = []
	for i in range(1,n+1):
		if i in completed:
			continue
		else:
			if chef == []:
				chef.append(i)
			else:
				if len(chef)>len(assistant):
					assistant.append(i)
				else:
					chef.append(i)
	print(*chef)
	print(*assistant)