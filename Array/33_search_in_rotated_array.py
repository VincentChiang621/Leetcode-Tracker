# Time: O(log(n))
# Space: O(1)
# binary search: use left sorted and right sorted; make cases 
# and update index as needed
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            # left sorted
            if nums[mid] - nums[l] >= 0:
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1