# Time: O(N)
# Space: O(1)
# if currentSum below 0, set to zero if above zero, add to result
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, currsum = -inf, 0
        start, end = -1, -1

        for i in range(len(nums)):
            if currsum == 0:
                start = i
            currsum += nums[i]
            if ans < currsum:
                ans = currsum
                end = i

            if currsum < 0:
                currsum = 0

        print(nums[start:end+1])
        return ans