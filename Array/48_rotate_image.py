# Time: O(n * m)
# Space: O(1)
# corners go to corners, use l,r pointers
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        ind = 0

        while l < r:
            for i in range(r - l):
                t, b = l, r
                n = matrix[b][r - i]

                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = n
            l += 1
            r -= 1