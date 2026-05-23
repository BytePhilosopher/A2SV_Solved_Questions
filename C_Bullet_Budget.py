from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    m = defaultdict(int)


    for hp, pos in zip(a, x):
        m[abs(pos)] += hp

    tot = 0
    kk = True

    for dist in sorted(m):
        tot += m[dist]

        if tot > dist * k:
            kk = False
            break

    print("YES" if kk else "NO")