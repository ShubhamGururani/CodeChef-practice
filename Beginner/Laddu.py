for _ in range(int(input())):
    num,nation = input().split()
    laddu = 0
    for _ in range(int(num)):
        ar = list(input().split())
        if ar[0] == 'CONTEST_WON':
            if int(ar[1]) <= 20:
                laddu += 300 + 20 - int(ar[1])
            else:
                laddu += 300
        elif ar[0] == 'TOP_CONTRIBUTOR':
            laddu += 300
        elif ar[0] == 'BUG_FOUND':
            laddu += int(ar[1])
        elif ar[0] == 'CONTEST_HOSTED':
            laddu += 50
    if nation == 'INDIAN':
        print(laddu//200)
    else:
        print(laddu//400)