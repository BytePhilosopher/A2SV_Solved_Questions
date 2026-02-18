# n=int(input())


# num=map(int,input().split())
# num=list(num)

# if n==1 and num[0]==1:
#     print(1)
#     exit()

# num.sort()


# ans=0
# for i in range(n,0,-1):
#     if i==num[i-1] or num[i-1]>i:
#         ans+=1
#         num.remove(num[i-1])
#         n-=1
#     else:
#         for j in range(i-1,n):
#             if num[j] == i or num[j]>i:
#                 ans+=1
#                 num.remove(num[j])
#                 n-=1
#                 break

# print(ans)

n = int(input())
num = list(map(int, input().split()))

num.sort()

ans = 0
idx = 0  # pointer to next unused contest

for day in range(1, n + 1):
    # move pointer until we find a contest >= day
    while idx < n and num[idx] < day:
        idx += 1
    
    if idx == n:
        break
    
    # use this contest
    ans += 1
    idx += 1  # mark as used by moving pointer

print(ans)
