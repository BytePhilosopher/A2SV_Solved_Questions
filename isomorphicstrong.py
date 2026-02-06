class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map:
                if hash_map[s[i]] != t[i]:
                    return False
            else:
                # Ensure no two chars map to the same char in t
                if t[i] in hash_map.values():
                    return False
                hash_map[s[i]] = t[i]
        return True
            