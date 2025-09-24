class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_val = float('inf')

    def push(self, val: int) -> None:
        # if val < self.min_val:
        #     self.min_val = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()