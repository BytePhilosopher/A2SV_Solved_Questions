# t=int(input())

# for _ in range(t):
#     n=int(input())
#     a_count=0
#     b_count=0
#     alice=True
#     cur=0

#     for i in range(1,n): 
#         if cur==0 and a_count+b_count==n:
#             a_count+=i
#             break
#         elif cur==2 and a_count+b_count==n:
#             b_count+=i
#             break

#         if alice:
#             a_count+=i
#             alice=False
#         else:
#             b_count+=i
#             cur+=1
#             if cur==2:
#                 alice=True
#                 cur=0
#     print(a_count,b_count)



t = int(input())
for _ in range(t):
    n = int(input())
    
    alice = 0
    bob = 0
    i = 1
    
    while n > 0:
        take = min(i, n)
        
        # Alice's turns when i % 4 == 1 or i % 4 == 0
        if i % 4 == 1 or i % 4 == 0:
            alice += take
        else:
            bob += take
        
        n -= take
        i += 1
    
    print(alice, bob)




