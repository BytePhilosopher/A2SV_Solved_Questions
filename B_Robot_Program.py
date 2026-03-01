import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    # Compute prefix sums
    pref = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'L':
            pref[i + 1] = pref[i] - 1
        else:
            pref[i + 1] = pref[i] + 1
    
    # Find first time reaching 0 from initial x
    first_hit = -1
    for i in range(1, n + 1):
        if x + pref[i] == 0:
            first_hit = i
            break
    
    # If never reaches 0 within k seconds
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    # First hit counted
    answer = 1
    remaining = k - first_hit
    
    # Find cycle length (first time pref[i] == 0)
    cycle = -1
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle = i
            break
    
    if cycle != -1:
        answer += remaining // cycle
    
    print(answer)