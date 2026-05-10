import sys

input = sys.stdin.readline

MAXT = 200000

n, k, q = map(int, input().split())

# Difference array
diff = [0] * (MAXT + 2)

# Read recipes
for _ in range(n):
    l, r = map(int, input().split())
    
    diff[l] += 1
    diff[r + 1] -= 1

# Build frequency array
freq = [0] * (MAXT + 2)

for i in range(1, MAXT + 1):
    freq[i] = freq[i - 1] + diff[i]

# good[i] = 1 if admissible
good = [0] * (MAXT + 2)

for i in range(1, MAXT + 1):
    if freq[i] >= k:
        good[i] = 1

# Prefix sum of admissible temperatures
pref = [0] * (MAXT + 2)

for i in range(1, MAXT + 1):
    pref[i] = pref[i - 1] + good[i]

# Answer queries
for _ in range(q):
    a, b = map(int, input().split())
    
    ans = pref[b] - pref[a - 1]
    
    print(ans)