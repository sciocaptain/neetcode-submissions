class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum[-1] >= val:
            self.minimum.append(val)

    def pop(self) -> None:
        last = self.stack.pop()
        if self.minimum[-1] == last:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
