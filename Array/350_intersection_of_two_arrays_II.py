# Time: O(m + n)
# Space: O(min(m,n))
# top, bottom, left, right for 2D traversal
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hmap = defaultdict(int)

        for i in nums1:
            hmap[i] += 1
        
        ans = []

        for num in nums2:
            if num in hmap and hmap[num] > 0:
                ans.append(num)
                hmap[num] -= 1
    
        return ans