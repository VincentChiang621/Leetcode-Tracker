# Time: O(n)
# Space: O(n)
# use a stack keep track of open parenthesis and pop if needed
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        parenmap = { ']': '[', '}': '{', ')': '(' }
        stack = []

        for c in s:
            if c in parenmap:
                if not stack or stack[-1] != parenmap[c]: #empty but close paren
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack