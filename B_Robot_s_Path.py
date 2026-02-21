n, k = map(int, input().split())
road = input()

count = 0

for ch in road:
    if ch == '#':
        count += 1
        if count >= k:
            print("NO")
            break
    else:
        count = 0
else:
    print("YES")