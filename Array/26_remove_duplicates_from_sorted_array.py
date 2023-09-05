# Time: O(n)
# Space: O(1)
# l pointer keeps track of non duplicates, r keeps track of duplicates
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 1


        while r < len(nums) and l < len(nums):
            if nums[r] == nums[r-1]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1

        return l