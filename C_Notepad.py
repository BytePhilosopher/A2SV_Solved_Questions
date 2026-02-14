

t = int(input())



for _ in range(t):
    n = int(input())
    s = input().strip()
    
   
    occcur = {}
    found = False
    
    
    for i in range(n - 1):
        pair = s[i:i+2]

        if pair in occcur:
            if occcur[pair] < i - 1:
                found = True
                break
        else:
            occcur[pair] = i
    
    if found:
        print("YES")
    else:
        print("NO")

