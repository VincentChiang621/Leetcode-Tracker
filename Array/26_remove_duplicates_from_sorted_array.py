# Time: O(n)
# Space: O(1)
# l pointer keeps track of non duplicates, r keeps track of duplicates
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == nums[l]:
                continue
            else:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]

        return l + 1