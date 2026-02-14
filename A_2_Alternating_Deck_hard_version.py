
t = int(input())
for _ in range(t):
    n = int(input())
    
    alice_w = 0
    alice_b = 0
    bob_w = 0
    bob_b = 0
    i = 1
    
    while n > 0:
        take = min(i, n)
        
        # Alice's turns when i % 4 == 1 or i % 4 == 0
        if i % 4 == 1 or i % 4 == 0:
            if take % 2 == 0:
                alice_w += take // 2
                alice_b += take // 2
            else:
                alice_w += take // 2 + 1
                alice_b += take // 2
        else:
            bob_w += take // 2
            bob_b += take // 2
            if take % 2 != 0:
                bob_b += 1

        n -= take
        i += 1
    
    print(alice_w, alice_b, bob_w, bob_b)
