for _ in range(int(input())):
	char = input().lower()
	if char == "b":
		print("BattleShip")
	elif char == "c":
		print("Cruiser")
	elif char == "d":
		print("Destroyer")
	else:
		print("Frigate")