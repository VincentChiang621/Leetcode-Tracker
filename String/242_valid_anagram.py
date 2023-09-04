class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = defaultdict(int)

        if len(s) != len(t):
            return False

        for c in s:
            hmap[c] += 1
        
        for test in t:
            hmap[test] -= 1
            if hmap[test] < 0:
                return False
        
        return True