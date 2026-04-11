
t = int(input())

def val(c):
    return ord(c) - ord('a')

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    w = input().strip()

    tr = sum(val(c) for c in w)

    win = sum(val(s[i]) for i in range(m))

    f = (win == tr)

    for i in range(m, n):
        win += val(s[i]) - val(s[i - m])
        if win == tr:
            f = True
            break

    print("YES" if f else "NO")