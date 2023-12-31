# Time: O(nlogn)
# Space: O(1) 
# sort by first val in interval, then append if non overlap, change val if do overlap
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        ans = intervals[0]

        for n in intervals:
            if ans[1] < n[0]:
                res.append(ans)
                ans = n
            else:
                ans[1] = max(ans[1], n[1])

        res.append(ans)

        return res
