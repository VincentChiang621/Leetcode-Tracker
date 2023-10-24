# Time: O(n)
# Space: O(n) 
# make a stack to monotonic decreasing 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = [] # of [val, index]

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < temperatures[i]:
                j = stack.pop()
                ans[j[1]] =  i - j[1]

            stack.append([n, i])
        
        return ans