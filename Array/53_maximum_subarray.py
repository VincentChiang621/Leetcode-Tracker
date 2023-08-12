# Time: O(N)
# Space: O(1)
# if currentSum below 0, set to zero if above zero, add to result
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currS = 0
        maxSub = nums[0]

        for n in nums:
            if currS < 0:
                currS = 0
            currS += n
            maxSub = max(maxSub, currS)

        return maxSub