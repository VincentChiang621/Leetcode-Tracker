# Time: O(n)
# Space: O(1) 
# put all roman chars into dict and then loop the string
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {}
        hashmap['I'] = 1
        hashmap['V'] = 5
        hashmap['X'] = 10
        hashmap['L'] = 50
        hashmap['C'] = 100
        hashmap['D'] = 500
        hashmap['M'] = 1000

        ans = hashmap[s[-1]]
        for i in range(len(s)-2, -1, -1):
            num = hashmap[s[i]]
            if num < hashmap[s[i+1]]:
                ans -= num
            else:
                ans += num
            
        return ans