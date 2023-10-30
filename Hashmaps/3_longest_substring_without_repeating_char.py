# Time: O(n)
# Space: O(n) 
# hmap to keep track of repeating chars and pop off when seen repeating
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cmap = {}
        l, ans = 0, 0
        for r in range(len(s)):
            if s[r] not in cmap:
                cmap[s[r]] = 1
            else:
                cmap[s[r]] += 1
           
            while cmap[s[r]] > 1:
                cmap[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans