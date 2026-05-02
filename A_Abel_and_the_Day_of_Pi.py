t = int(input())
pi = "314159265358979323846264338327"

for _ in range(t):
    n = input().strip()
    count = 0
    
    for i in range(min(len(n), len(pi))):
        if n[i] == pi[i]:
            count += 1
        else:
            break
    
    print(count)