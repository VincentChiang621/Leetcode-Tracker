# Time: O(n)
# Space: O(1) 
# constant memory! keep pointer to the two numbers; f(n) = f(n-2) + f(n-1)
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-2) + f(n-1)
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one