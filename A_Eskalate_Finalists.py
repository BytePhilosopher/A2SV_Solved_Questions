import sys
sys.setrecursionlimit(10**7)
k=int(input())
applicant=list(map(int,input().split()))

_max=max(applicant)

if _max>25:
    print(_max-25)
else:
    print(0)
