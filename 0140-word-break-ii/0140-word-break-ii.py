class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == n:
                return [""]   # important base case

            res = []

            for j in range(i, n):
                word = s[i:j+1]
                if word in wordDict:
                    sub_sentences = dfs(j+1)

                    for sub in sub_sentences:
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)

            memo[i] = res
            return res

        return dfs(0)