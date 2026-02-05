class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res={}
        for i in range(len(list1)):
            if list1[i] in list2:
                j=list2.index(list1[i])
                res[list1[i]]=(i+j)
        minval=min(res.values())
        keys=[key for key,val in res.items() if val==minval]

        return keys
        

        