class Solution:
    def longestPalindrome(self, s: str) -> str:

        def PaliCount(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        left, right = 0, 0
        for i in range(len(s)):
            len1 = PaliCount(i, i)
            len2 = PaliCount(i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > (right - left):
                right = i + (maxlen // 2)
                left = i - ((maxlen - 1) // 2)
            
        return s[left:right + 1]