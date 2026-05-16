t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    b = sorted(a)

    if 2 * x <= n:
        print("YES")
    else:
        ok = True

        for i in range(n - x, x):
            if a[i] != b[i]:
                ok = False
                break

        print("YES" if ok else "NO")