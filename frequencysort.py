class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        
        unique_chars = list(freq.keys())
        unique_chars.sort(key=lambda x: freq[x], reverse=True)

    
        result = []
        for char in unique_chars:
            result.append(char * freq[char])

        return ''.join(result)