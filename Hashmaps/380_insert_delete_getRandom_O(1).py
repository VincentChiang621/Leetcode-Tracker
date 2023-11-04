# Time: O(1)
# Space: O(n) 
# set and list, list for the getRandom number
class RandomizedSet:

    def __init__(self):
        self.rset = {}
        self.rlist = []

    def insert(self, val: int) -> bool:
        res = val not in self.rset
        # val not in rset
        if res:
            self.rset[val] = len(self.rlist)
            self.rlist.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.rset
        if res:
            ind = self.rset[val]
            last = self.rlist[-1]
            self.rlist[ind] = last
            self.rlist.pop()
            self.rset[last] = ind
            del self.rset[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.rlist)