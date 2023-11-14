# Time: O(n)
# Space: O(n) 
# Recursive: create helper function the ans[] is almost like a "global" variable
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def postorder(root):
            if root == None:
                return
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)

        postorder(root)
        return ans
