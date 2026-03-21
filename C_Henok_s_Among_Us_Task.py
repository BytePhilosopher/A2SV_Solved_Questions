def R():
    a, b = map(int, input().split())
    ans = [b]

    while b > a:
        if b % 10 == 1:
            b = (b - 1) // 10
            ans.append(b)
        elif b % 2 == 0:
            b = b // 2
            ans.append(b)
        else:
            print("NO")   # print NO instead of just return
            return

    if b == a:
        print("YES")
        ans.reverse()
        print(len(ans))
        print(*ans)
    else:
        print("NO")

if __name__ == "__main__":
    R()