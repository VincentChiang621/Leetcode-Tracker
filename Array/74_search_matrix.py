# Time: O(m + n)
# Space: O(1)
# start at bottom left corner, if target smaller go up, if target bigger go right
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        currRows = numRows - 1
        currCols = 0

        while currRows >= 0 and currCols <= numCols - 1:
            if target == matrix[currRows][currCols]:
                return True
            elif target > matrix[currRows][currCols]:
                currCols += 1
            else:
                currRows -= 1
        
        return False