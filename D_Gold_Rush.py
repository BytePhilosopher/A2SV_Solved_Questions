import sys
sys.setrecursionlimit(10**7)
t=int(input())
def c(x,t):
    if x==t:
        return True
    if x<t or x%3!=0:
        return False
    
    y=x//3
    
    res=c(y,t) or c(2*(y),t)

    return res


for _ in range(t):
    n,m=map(int,input().split())
    
    print("YES" if c(n,m) else "NO")