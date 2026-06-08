class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less,greater=[],[]
        cnt=0

        for n in nums:
            if n< pivot:
                less.append(n)
            elif n>pivot:
                greater.append(n)
            else:
                cnt+=1
        return (less)+([pivot]*cnt)+(greater)