class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        store = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        val = 0
        i = len(s) - 1

        while i >= 0:
            # make sure we don't go out of range when checking j = i - 1
            if i > 0 and s[i] == "X" and s[i - 1] == "I":
                val += 9
                i -= 2
            elif i > 0 and s[i] == "V" and s[i - 1] == "I":
                val += 4
                i -= 2
            elif i > 0 and s[i] == "L" and s[i - 1] == "X":
                val += 40
                i -= 2
            elif i > 0 and s[i] == "C" and s[i - 1] == "X":
                val += 90
                i -= 2
            elif i > 0 and s[i] == "D" and s[i - 1] == "C":
                val += 400
                i -= 2
            elif i > 0 and s[i] == "M" and s[i - 1] == "C":
                val += 900
                i -= 2
            else:
                val += store.get(s[i])
                i -= 1

        return val