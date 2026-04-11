

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    size = 2 ** n

    ans = a[:]
    seg = 2

    for _ in range(n):
        new_ans = ans[:]

        for start in range(0, size, seg):
            block = list(range(start, start + seg))

            # sort indices by value
            block.sort(key=lambda x: ans[x])

            # all pairs in sorted order
            for i in range(seg):
                for j in range(i + 1, seg):
                    if ans[block[i]] < ans[block[j]]:
                        new_ans[block[j]] += 1
                    elif ans[block[i]] > ans[block[j]]:
                        new_ans[block[i]] += 1

        ans = new_ans
        seg *= 2

    print(*ans)