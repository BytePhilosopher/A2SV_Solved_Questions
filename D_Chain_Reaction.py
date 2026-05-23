t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    s = input().strip()


    if '1' not in s:
        print(0)
        continue

    ans = a
    i = 0
    n = len(s)

    while i < n:
        if s[i] == '1':
            i += 1
        else:
            j = i
            while j < n and s[j] == '0':
                j += 1


            if i > 0 and j < n and s[i - 1] == '1' and s[j] == '1':
                gap = j - i
                ans += min(a, gap * b)

            i = j

    print(ans)