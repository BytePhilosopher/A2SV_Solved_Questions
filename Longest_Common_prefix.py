class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            # shrink prefix until it matches the beginning of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix