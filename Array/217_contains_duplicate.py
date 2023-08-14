# Time: O(N)
# Space: O(1)
# iterate array store element as key in hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for n in nums:
            if n in numMap:
                numMap[n] += 1
            else:
                numMap[n] = 1
            
            if numMap[n] == 2:
                return True
        return False