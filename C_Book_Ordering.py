n = int(input())

w, h = map(int, input().split())
prev = max(w, h)

possible = True

for _ in range(n - 1):
    w, h = map(int, input().split())
    
    big = max(w, h)
    small = min(w, h)
    
    if big <= prev:
        prev = big
    elif small <= prev:
        prev = small
    else:
        possible = False
        break

print("YES" if possible else "NO")