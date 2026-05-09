class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1

        # Step 2: Overwrite nums in sorted order
        i = 0
        for color in range(3):           # only 0,1,2
            for j in range(count[color]):
                nums[i] = color
                i += 1
        