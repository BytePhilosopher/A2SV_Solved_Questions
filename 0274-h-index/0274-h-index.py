class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        ans=0

        maximum = max(citations)
        count = [0] * (maximum + 1)

        for num in citations:
            count[num] += 1

       
        for index, value in enumerate(count):
            total_sum=0
            start_summing=False

            for key, val in enumerate(count):
                if key == index:
                    start_summing = True
                    continue  

                if start_summing:
                    total_sum += val
            if index<=total_sum+count[index]:
                ans=max(ans,index)
            print(total_sum,index)


        return ans if ans else  sum(x != 0 for x in citations)
    

       