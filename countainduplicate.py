class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _dict=dict()
        for n in nums:
            _dict[n]=_dict.get(n,0)+1
        for val in _dict.values():
            if val>=2:
                return True
        return False
        