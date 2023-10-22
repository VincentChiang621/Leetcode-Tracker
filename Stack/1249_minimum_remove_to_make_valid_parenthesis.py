# Time: O(n)
# Space: O(n) 
# go through string once from left to right, then from right to left
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ''
        stack = []
        for i in range(len(s)):
            if len(stack) == 0 and s[i] == ')':
                continue
            elif s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop()
            ans += s[i]

        s2 = []
        res = ''
        for i in range(len(ans)-1, -1, -1):
            if len(s2) == 0 and ans[i] == '(':
                continue
            elif ans[i] == ')':
                s2.append(')')
            elif ans[i] == '(':
                s2.pop()
            res += ans[i]

        return res[::-1]