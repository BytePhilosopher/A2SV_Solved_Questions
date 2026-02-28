# from collections import Counter
# t=int(input())

# for _ in range(t):
#     n,k=map(int,input().split())
#     d=list(map(int,input().split()))

#     count=Counter(d)
#     cards=sorted(count.keys())

#     m,num_card,l=0,0,0
#     for r in range(len(cards)):
#         num_card+=count[cards[r]]

#         while r>l and cards[r]-cards[r-1]>1 or r-l+1>k:
#             num_card-=count[cards[l]]
#             l+=1
#         m=max(m,num_card)
    
#     print(m)




# import sys

# # sys.setrecursionlimit(10**6)
# from collections import *
# from bisect import bisect_left, bisect_right
# from copy import deepcopy
# from random import randint
# from math import *
# from heapq import *

# # input = input
# input = sys.stdin.readline


# def solve():
#     n, k = list(map(int, input().split()))
#     nums = list(map(int, input().split()))
#     nums.sort()

#     l = 0
#     ans = 1
#     cnt = defaultdict(int)
#     cnt[nums[0]] += 1

#     for r in range(1, n):

#         if nums[r] - nums[r - 1] > 1:
#             l = r
#             cnt.clear()
#         cnt[nums[r]] += 1

#         while len(cnt) > k:
#             cnt[nums[l]] -= 1
#             if cnt[nums[l]] == 0:
#                 del cnt[nums[l]]
#             l += 1
#         ans = max(ans, r - l + 1)

#     print(ans)


# def main():
#     t = int(input())

#     for _ in range(t):
#         solve()


# if __name__ == "__main__":
#     main()




t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    

    count = {}
    for x in d:
        count[x] = count.get(x, 0) + 1

    cards = sorted(count.keys())

    l = 0
    num_card = 0
    ans = 0

    for r in range(len(cards)):

        if r > 0 and cards[r] != cards[r - 1] + 1:
            l = r
            num_card = 0

        num_card += count[cards[r]]


        while r - l + 1 > k:
            num_card -= count[cards[l]]
            l += 1

        ans = max(ans, num_card)

    print(ans)
