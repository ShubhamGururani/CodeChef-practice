friends = 0
for _ in range(int(input())):
	s = input()
	substr = ["ch","he","ef","che","hef","chef"]
	for item in substr:
		if item in s:
			friends += 1
			break
print(friends)