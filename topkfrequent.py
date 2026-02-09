class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        num=Counter(nums)
        lis=num.most_common(k)
        ans=[]

        for idx in range(len(lis)):
            ans.append(lis[idx][0])
            
        return ans
        