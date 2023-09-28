# Time:O(N)
# Space:O(1)
# l points to == val while r points to != val and swaps
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0
        
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            
        return l