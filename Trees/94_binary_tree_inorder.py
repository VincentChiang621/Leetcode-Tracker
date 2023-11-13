# Time: O(n)
# Space: O(n) 
# Recursive: create helper function the ans[] is almost like a "global" variable
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left -> do -> right
        ans = []
        def inorder(rootIn):
            if not rootIn:
                return 
            inorder(rootIn.left)
            ans.append(rootIn.val)
            inorder(rootIn.right)
        inorder(root)
        return ans