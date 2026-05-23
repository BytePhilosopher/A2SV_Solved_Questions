t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if n % 2 == 1:

        w = False

        for i in range(0, n, 2):   
            if int(s[i]) % 2 == 1:
                w = True

        print(1 if w else 2)

    else:

        w = False

        for i in range(1, n, 2):  
            if int(s[i]) % 2 == 0:
                w = True

        print(2 if w else 1)