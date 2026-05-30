t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a[i] > a[(i + 1) % n]:
            cnt += 1

    print("Yes" if cnt <= 1 else "No")