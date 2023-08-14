# Time: O(N)
# Space: O(1)
# left and right pointer; left always points to smallest and right keeps indexing
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

        return maxP
            