# Time: O(n)
# Space: O(n) 
# stack and join string with ''.join(stack)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
            
        return ''.join(stack)