t = int(input())

for _ in range(t):
    a, x, y = map(int, input().split())

    if a < min(x, y) or a > max(x, y):
        print("YES")
    else:
        print("NO")