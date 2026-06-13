class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for word in words:
            temp=0
            for ch in word:
                temp+=weights[ord(ch)-97]
            # print(temp%26)
            res+=chr(90-(temp%26))
        return res.lower()
        