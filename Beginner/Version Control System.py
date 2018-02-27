import sys
import math
 
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    a=set(map(int,input().split()))
    b=set(map(int,input().split()))
    print(len(a.intersection(b)),n-len(a.union(b)))