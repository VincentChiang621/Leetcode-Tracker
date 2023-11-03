# Time: O(n)
# Space: O(1) 
# we know the sum should be n(n-1)/2 + n, so we just subtract the actual sum from that
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = n*(n-1)//2 + n
        arrS = 0
        for n in nums:
            arrS += n
        return summ - arrS
