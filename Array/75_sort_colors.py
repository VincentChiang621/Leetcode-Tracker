# Time: O(N)
# Space: O(1)
# l,r,curr pointers and swap/index when needed
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0        # Pointer for 0s
        high = len(nums) - 1   # Pointer for 2s
        curr = 0       # Current position

        while curr <= high:
            if nums[curr] == 2:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1
            elif nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                curr += 1
                low += 1
            elif nums[curr] == 1:
                curr += 1


            