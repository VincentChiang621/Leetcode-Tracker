# Time: O(n*m)
# Space: O(n*m) 
# DP curr = bottom + right
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]

        def fillmemo(m, n):
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if j + 1 == n or i + 1 == m:
                        memo[i][j] = 1
                    else:
                        memo[i][j] = memo[i][j+1] + memo[i+1][j]

            
        fillmemo(m,n)
        return memo[0][0]