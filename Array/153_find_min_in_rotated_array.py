# Time: O(log(n))
# Space: O(1) 
# binary search: make cases
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            ans = min(ans, nums[m])
            if nums[m] < nums[r] or nums[l] < nums[r]:
                r = m - 1
            else:
                l = m + 1
            
        return ans

class Solution1:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[0]

        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                smallest = min(smallest, nums[l])
                l = m + 1
            else:
                smallest = min(smallest, nums[m])
                r = m - 1
        
        return smallest