# Time: O(n)
# Space: O(1) 
# var have and need for constant checks, update dict when see characters. 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap, tmap = {}, {}

        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        
        have, need = 0, len(tmap)
        res = ""
        l = 0

        for r in range(len(s)):
            c = s[r]
    
            if c in tmap:
                smap[c] = 1 + smap.get(c, 0)
                if smap[c] == tmap[c]:
                    have += 1
            
            while need == have:
                if res == "" or len(res) > (r - l + 1):
                    res = s[l:r+1]
                if s[l] in smap:
                    smap[s[l]] -= 1
                    if smap[s[l]] < tmap[s[l]]:
                        have -= 1
                l += 1

            r += 1

        return res