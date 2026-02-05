class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        freqchar={}
        freqword={}
        ans=[]
        for c in chars:
            freqchar[c]=freqchar.get(c,0)+1
        for word in words:
            for w in word:
                freqword[w]=freqword.get(w,0)+1
            check=0
            for key, val in freqword.items():
                if val>freqchar.get(key,0):
                    break
            else:
                ans.append(word)
            freqword.clear()
        sum=0
        for i in range(len(ans)):
            sum+=len(ans[i])
        return sum

        