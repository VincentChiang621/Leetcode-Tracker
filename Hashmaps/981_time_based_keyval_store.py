# Time: set=O(1) get=O(logn)
# Space: O(n) 
# hashmap[key] to [timestamp, val]; then use binary search to find matching timestamp
class TimeMap:

    def __init__(self):
        self.keytoTime = {} # key: list of [timestamp, val]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keytoTime:
            self.keytoTime[key] = []
        self.keytoTime[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.keytoTime.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return res