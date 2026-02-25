class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans=[]
        count=Counter(s)
        
        l,min_idx=0,0
        flag=0
        # "ababcbaca defegdehijhklij"
        
        while l<len(s):
            right=len(s)-1
            while l<=right:
                if s[l]==s[right]:
                    min_idx=right
                    break
                right-=1
            check=True
        
            # print(flag,min_idx, l)
            cm=Counter(s[flag:min_idx+1])
            # print(count,cm)
            for key,val in cm.items():
                if count[key]!=val:
                    l+=1
                    check=False
                    break
            if check:
                ans.append(len(s[flag:min_idx+1]))
                flag=min_idx+1
                l=min_idx+1

        return ans





            




        
        