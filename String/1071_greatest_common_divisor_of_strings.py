# Time: O(min(m,n) * (m+n))
# Space: O(1)
# check if a substring is divisor, if it is, update answer
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        ans = ''
        def isDivisor(string):
            if len1 % len(string) != 0 or len2 % len(string) != 0:
                return False
            f1, f2 = len1 // len(string), len2 // len(string)

            if f1 * string == str1 and f2 * string == str2:
                return True


        for i in range(1, min(len1, len2)+1):
            if isDivisor(str1[:i]):
                ans = str1[:i]
        
        return ans

        