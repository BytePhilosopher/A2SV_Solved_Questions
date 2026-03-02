class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=nums


    def sumRange(self, left: int, right: int) -> int:
        _sum=0
        for s in range(left,right+1):
            _sum+=self.arr[s]

        return _sum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)