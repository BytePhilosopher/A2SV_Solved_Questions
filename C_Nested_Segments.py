n = int(input())
segments = []

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r, i + 1))  



segments.sort(key=lambda x: (x[0], -x[1]))

max_right = segments[0][1]
max_index = segments[0][2]

for i in range(1, n):
    l, r, idx = segments[i]

    if r <= max_right:
        print(idx, max_index)
        exit()

    if r > max_right:
        max_right = r
        max_index = idx

print(-1, -1)
