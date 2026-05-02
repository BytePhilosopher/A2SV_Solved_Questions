import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1

    
    from collections import Counter
    counts = Counter(degree[1:])

 
    val = []
    for deg, count in counts.items():
        if deg != 1:
            val.append((deg, count))

   
    if len(val) == 2:
        if val[0][1] == 1:
            x = val[0][0]
            y = val[1][0] - 1
        else:
            x = val[1][0]
            y = val[0][0] - 1
        print(x, y)
    
   
    else:
        x = val[0][1] - 1
        y = val[0][0] - 1
        print(x, y)


t = int(input())
for _ in range(t):
    solve()