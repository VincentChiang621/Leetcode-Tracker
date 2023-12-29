# Time: O(n*m)
# Space: O(1) or O(n*m) depending if you count output or not
# create output, then swap i,j with j,i
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0] * ROWS for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                res[j][i] = matrix[i][j]
        
        return res