# Time: O(n)
# Space: O(1)
# Moores voting algorithm for majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == ans:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                ans = nums[i]
                count = 1
                
        return ans