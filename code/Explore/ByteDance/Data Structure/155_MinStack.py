class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.queue.append((x, curMin))

    def pop(self) -> None:
        self.queue.pop()

    def top(self) -> int:
        if not len(self.queue):
            return None
        else:
            return self.queue[-1][0]

    def getMin(self) -> int:
        if not len(self.queue):
            return None
        else:
            return self.queue[-1][1]