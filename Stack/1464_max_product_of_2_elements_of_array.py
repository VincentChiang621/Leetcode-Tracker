# Time: O(n^2)
# Space: O(1) 
# brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = (nums[i]-1)*(nums[j]-1)
                maxP = max(maxP, product)

        return maxP

# Time: O(nlogn)
# Space: O(1) 
# sort and then return last two elements product
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)
    
# Time: O(n)
# Space: O(1) 
# l,r pointers at both ends and move closer
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        maxP = 0
        while l < r:
            maxP = max(maxP, (nums[l]-1)*(nums[r]-1))
            if nums[l] <= nums[r]:
                l += 1
            else:
                r -= 1

        return maxP
