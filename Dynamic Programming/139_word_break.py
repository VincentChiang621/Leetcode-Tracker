# Time: O(len(s) * len(s) * len(worddict)
# Space: O(len(s))
# use 1D array to store whether s[ i ] can be formed check dp[ 0 ]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (len(word) <= (len(s) - i) and word == s[i: i + len(word)]):
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        
        return dp[0]