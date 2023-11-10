# Time: O(n)
# Space: O(n) 
# hashmap for a prefix sum (aka how many times that num can be chopped off from out currSum), one pass
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = { 0 : 1 }
        currSum = 0
        res = 0

        for n in nums:
            currSum += n
            target = currSum - k
            
            res += preSum.get(target, 0)

            preSum[currSum] = 1 + preSum.get(currSum, 0)

        return res