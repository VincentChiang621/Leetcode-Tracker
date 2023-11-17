# Time: O(n)
# Space: O(n) 
# dfs on left and right, base cases are important
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 2 null trees are ==
        if not p and not q:
            return True
        # implies 1 null tree and one not null
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right