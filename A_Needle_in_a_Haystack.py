from collections import Counter

t = int(input())
for _ in range(t):
    s = input().strip()
    n = input().strip()

    count_s = Counter(s)
    count_n = Counter(n)

    # Check possibility
    possible = True
    for ch in count_s:
        if count_n[ch] < count_s[ch]:
            print("Impossible")
            possible = False
            break

    if not possible:
        continue

    # Remove s characters from n
    for ch in s:
        count_n[ch] -= 1

    # Build remaining sorted string
    remaining = []
    for ch in sorted(count_n.elements()):
        remaining.append(ch)

    remaining = "".join(remaining)

    # Find insertion position
    pos = len(remaining)
    for i in range(len(remaining)):
        if remaining[i] > s[0]:
            pos = i
            break

    # Construct answer
    ans = remaining[:pos] + s + remaining[pos:]

    print(ans)