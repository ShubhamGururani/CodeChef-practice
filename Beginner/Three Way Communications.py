import math
for _ in range(int(input())):
	dist = int(input())
	chef = [int(i) for i in input().split()]
	server = [int(i) for i in input().split()]
	sous = [int(i) for i in input().split()]
	d1 = math.sqrt(pow(server[0]-chef[0],2)+pow(server[1]-chef[1],2))
	d2 = math.sqrt(pow(sous[0]-chef[0],2)+pow(sous[1]-chef[1],2))
	d3 = math.sqrt(pow(server[0]-sous[0],2)+pow(server[1]-sous[1],2))
	if (d1 <= dist and d2 <= dist and d3 <= dist) or (d1 > dist and d2 <= dist and d3 <= dist) or (d2 > dist and d1 <= dist and d3 <= dist) or (d3 > dist and d1 <= dist and d2 <= dist):print("yes")
	else:print("no")