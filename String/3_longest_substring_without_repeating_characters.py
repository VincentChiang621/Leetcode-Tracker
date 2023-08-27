# Time: O(n)
# Space: O(n)
# sliding window and adjust windows if we see repeating chars
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcabcbb
        
        charSet = set()
        l = longest = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, len(charSet))

        return longest
            