class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s={}
        counter_t={}

        for index in range(len(s)):
            counter_s[s[index]]=counter_s.get(s[index],0)+1
        
        for index_t in range(len(t)):
            counter_t[t[index_t]]=counter_t.get(t[index_t],0)+1
        

        return counter_s==counter_t


        