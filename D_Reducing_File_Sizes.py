n, m = map(int, input().split())

files = []
for _ in range(n):
    a, b = map(int, input().split())
    files.append((a, b))

total = sum(a for a, b in files)

if total <= m:
    print(0)
    exit()

intervals = [a - b for a, b in files]
intervals.sort(reverse=True)

count = 0

for save in intervals:
    total -= save
    count += 1
    if total <= m:
        print(count)
        break
else:
    print(-1)