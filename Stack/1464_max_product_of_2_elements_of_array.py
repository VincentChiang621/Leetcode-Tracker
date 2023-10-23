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
    
