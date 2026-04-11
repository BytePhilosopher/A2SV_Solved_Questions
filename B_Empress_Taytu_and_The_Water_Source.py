import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    def can(s):
        tot = 0
        for i in range(n):
            tr = (d[i] + s - 1) // s
            tot += tr * a[i]
            if tot > k:
                return False
        return True

    
    if sum(a) > k:
        print(-1)
        continue

    l, r = 1, max(d)
    ans = -1

    while l <= r:
        mid = (l + r) // 2
        if can(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans)