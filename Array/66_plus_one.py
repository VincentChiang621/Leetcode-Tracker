# Time: O(n)
# Space: O(1)
# if val = 9, make it 0 and loop until we find non 9, then just return add 1,
# or all values are 9 and you make all 9s zero and append 1 in front
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            
        return [1] + digits