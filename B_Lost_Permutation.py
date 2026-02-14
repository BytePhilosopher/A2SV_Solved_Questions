
t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    arr = list(map(int, input().split()))

    total = sum(arr)
    mx = max(arr)
    
    n = mx
    # Increase n until triangular sum reaches or exceeds total + s
    while n * (n + 1) // 2 < total + s:
        n += 1
    
    if n * (n + 1) // 2 == total + s:
        print("YES")
    else:
        print("NO")
