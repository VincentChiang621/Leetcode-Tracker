# Time: O(1)
# Space: O(n) 
# use og stack and a min stack, operations can be done in O(1) time
class MinStack:

    def __init__(self):
        self.stack = []
        self.mintracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mintracker) == 0 or self.mintracker[-1] > val:
            self.mintracker.append(val)
        else:
            self.mintracker.append(self.mintracker[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mintracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mintracker[-1]