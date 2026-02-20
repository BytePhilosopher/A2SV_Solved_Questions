class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1)!=len(word2):
            return False

        counter_w1=Counter(word1)
        counter_w2=Counter(word2)


        countW1=[val for val in counter_w1.values()]
        countw2=[val for val in counter_w2.values()]

        keyw1=[key for key in counter_w1.keys()]
        keyw2=[key for key in counter_w2.keys()]


        if sorted(countW1)==sorted(countw2) and sorted(keyw2)==sorted(keyw1):
            return True

        return False
        