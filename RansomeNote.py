class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count=Counter(magazine)
        counted=Counter(ransomNote)

        for key in counted.keys():
            if key not in count or counted[key]>count[key]:
                return False

        return True
        