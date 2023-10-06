# Time: O(n)
# Space: O(1)
# l,r pointers: check who is smaller and the move pointer 
# finds the maximum in a greedy way
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxW = 0

        while r > l: 
            water = min(height[l], height[r]) * (r-l)
            maxW = max(maxW, water)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxW