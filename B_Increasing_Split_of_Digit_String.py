t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    if n==2:
        if s[0]<s[1]:
            print("YES")
            print(s[0],s[1])
        else:
            print("NO")
    else:
        print("YES")
        print(2)
        print(s[0],s[1:])

    
