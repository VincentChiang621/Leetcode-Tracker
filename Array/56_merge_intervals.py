# Time: O(nlogn)
# Space: O(1) 
# sort by first val in interval, then append if non overlap, change val if do overlap
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        def compare(val):
            return val[0]

        intervals.sort(key=compare)

        output.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])

        return output