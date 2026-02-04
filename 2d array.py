class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges = sorted(ranges, key=lambda l: l[0])
        ans=[]
        check=0
        for ind in range(left,right+1):
            for rang in ranges:
                if ind in range(rang[0],rang[1]+1) and ind not in ans:
                    check+=1
                    ans.append(ind)
            if check==(right-left+1):
                return True
        return False   
        