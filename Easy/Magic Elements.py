for _ in range(int(input())):
  n , k = map(int,input().split())
  ar = list(map(int,input().split()))
  count = 0
  arSum = sum(ar)
  for i in ar:
    part = arSum - i
    x = i + k
    if x > part:
      count += 1
  print(count)