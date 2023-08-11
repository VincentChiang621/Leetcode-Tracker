#Time: O(N^3)
#Space: O(1)
#triple for-loop to check all triplet subsequences
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        
        return False

#Time: O(N)
#Space: O(1)
#one pass, if curr < first then first = curr; 
#          elif curr < second then second = curr
#          else curr is bigger than first and second; return True
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if first >= n:
                first = n
            elif second >= n:
                second = n
            else:
                return True