class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset,curset=[],[]
        n=len(nums)

        def subsets(i,curset):
            if i>=len(nums):
                subset.append(curset[:])
                return


            curset.append(nums[i])
            subsets(i+1,curset)


            curset.pop()
            print(curset)

            subsets(i+1,curset)
            return

        subsets(0,curset)
        return subset