# Time: O(n^2)
# Space: O(1)
# sort array first, keep first 'i' constant and use 2sum. 
# Since sorted, check for dup by seeing left.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                threesome = nums[i] + nums[l] + nums[r]
                if threesome > 0:
                    r -= 1
                elif threesome < 0:
                    l += 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res
                    