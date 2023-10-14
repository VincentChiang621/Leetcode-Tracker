# Time: O(n)
# Space: O(1)
# l,r pointers: swap when l == 0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1