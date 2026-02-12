class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        get=[]
        for n in nums1:
            for x in nums2:
                if n==x and n not in get:
                    get.append(n)
        return get
        