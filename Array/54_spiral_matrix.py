# Time: O(right * bottom)
# Space: O(1)
# top, bottom, left, right for 2D traversal
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        ans = []
        while len(ans) < (len(matrix[0])*len(matrix)):
            # go right
            for i in range(left ,right):
                ans.append(matrix[top][i])
            top += 1
            # go down
            for j in range(top, bottom):
                ans.append(matrix[j][right-1])
            right -= 1
            if top >= bottom or left >= right:
                break
            # go left
            for k in range(right-1, left-1, -1):
                ans.append(matrix[bottom -1][k])
            bottom -= 1
            # go up
            for l in range(bottom-1, top-1, -1):
                ans.append(matrix[l][left])
            left += 1
        
        return ans
        