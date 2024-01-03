# Time: O(n)
# Space: O(n) 
# maintain upper and lower bounds. solve with dfs
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, upper, lower):
            if not root:
                return True

            if root.val >= upper or root.val <= lower:
                return False

            return dfs(root.left, root.val, lower) and dfs(root.right, upper, root.val)

        return dfs(root.left, root.val, float("-inf")) and dfs(root.right, float("inf"), root.val)