class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern=list(pattern)
        container={}
        s=s.split()

        if len(s)!=len(pattern):
            return False

        for i in range(len(s)):
            if pattern[i] in container and container[pattern[i]]!=s[i]:
                return False
            key=[k for k,v in container.items() if v==s[i]]
            if s[i] in container.values() and [pattern[i]]!=key:
                return False
            container[pattern[i]]=s[i]
            print(container)


 
        return True