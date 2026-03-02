import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    

    balance = [0] * n
    count = 0
    for i in range(n):
        if a[i] == '1':
            count += 1
        else:
            count -= 1
        balance[i] = count
    
    flip = 0
    possible = True
    
    for i in range(n - 1, -1, -1):
        current = a[i]
        
        if flip:
            current = '1' if current == '0' else '0'
        
        if current != b[i]:
            if balance[i] != 0:
                possible = False
                break
            flip ^= 1
    
    print("YES" if possible else "NO")