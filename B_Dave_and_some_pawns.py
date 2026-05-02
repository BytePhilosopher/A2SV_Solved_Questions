import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    e = input().strip()
    d = input().strip()

    r = 0
    o = [False] * n

    for i in range(n):
        if d[i] == '0':
            continue

   
        if i > 0 and e[i - 1] == '1' and not o[i - 1]:
            r += 1
            o[i - 1] = True

  
        elif e[i] == '0' and not o[i]:
            r += 1
            o[i] = True

    
        elif i < n - 1 and e[i + 1] == '1' and not o[i + 1]:
            r += 1
            o[i + 1] = True

    print(r)


t = int(input())
for _ in range(t):
    solve()