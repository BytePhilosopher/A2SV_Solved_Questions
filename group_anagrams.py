class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash={}
        if not strs or len(strs)==1:
            return [strs] 
        for s in strs:
            key=tuple(sorted(s))
            if key not in hash:
                hash[key]=[s]
            else:
                hash[key].append(s)


            
        return  [ans for ans in hash.values()]
        