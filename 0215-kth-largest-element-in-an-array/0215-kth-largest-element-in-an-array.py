class Solution:
    def findKthLargest(self, nums, k):
        n=len(nums)
        from heapq import heapify, heappop
       
        heapify(nums)
        for i in range(n-k):
            heappop(nums)
            
        return heappop(nums)
