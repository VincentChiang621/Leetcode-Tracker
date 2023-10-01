# Time: O(log(n))
# Space: O(1)
# binary search: use left sorted and right sorted; make cases 
# and update index as needed
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[r] == target:
                return r
            # first half increasing
            if nums[m] > nums[l]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            # second half increasing
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1