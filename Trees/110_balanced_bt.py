# Time: O(n)
# Space: O(n) 
# dfs function that returns [height, bool(balanced)]
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [0, True]
            l = dfs(root.left)
            r = dfs(root.right)
            bal = abs(l[0]-r[0]) <= 1 and l[1] and r[1]

            return [1 + max(l[0], r[0]), bal]

        return dfs(root)[1]