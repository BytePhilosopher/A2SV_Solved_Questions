class Solution:
    def findKthLargest(self, nums, k):

        offset = 10000
        size = 20001

        count = [0] * size

        # build frequency
        for num in nums:
            count[num + offset] += 1

        # scan from largest to smallest
        for i in range(size - 1, -1, -1):

            k -= count[i]

            if k <= 0:
                return i - offset