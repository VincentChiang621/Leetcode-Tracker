class Solution:
    def longestPalindrome(self, s: str) -> int:
        cmap = {}
        longest = 0

        for c in s:
            if c not in cmap or cmap[c] == 0:
                cmap[c] = 1
            elif cmap[c] == 1:
                cmap[c] = 0
                longest += 2
        
        for key,value in cmap.items():
            if value == 1:
                return longest + 1

        return longest
