class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dict1=Counter(s)
        dict2=Counter(t)

        for key,value in dict1.items():
            if value!=dict2[key]:
                return False
        
        return True