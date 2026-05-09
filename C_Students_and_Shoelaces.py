from collections import deque


n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    deg[a] += 1
    deg[b] += 1

q = deque()

for i in range(1, n + 1):
    if deg[i] == 1:
        q.append(i)

ans = 0

while q:
    size = len(q)
    removed = False

    for _ in range(size):
        node = q.popleft()

        if deg[node] != 1:
            continue

        removed = True
        deg[node] = 0

        for nei in adj[node]:
            if deg[nei] > 0:
                deg[nei] -= 1

                if deg[nei] == 1:
                    q.append(nei)

    if removed:
        ans += 1

print(ans)