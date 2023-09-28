# Time: O(row*col)
# Space: O(row+col)
# add which rows and cols have zeros into 2 sets, then make them zero.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numset1 = set()
        numset2 = set()

        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if matrix[m][n] == 0:
                    numset1.add(m)
                    numset2.add(n)
                
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if m in numset1 or n in numset2:
                    matrix[m][n] = 0