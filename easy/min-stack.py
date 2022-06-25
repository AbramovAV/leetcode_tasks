class MinStack:

    def __init__(self):
        self.values = {}

    def push(self, val: int) -> None:
        if not self.values:
            self.values[len(self.values)] = (val, val)
        else:
            self.values[len(self.values)] = (val,
                                            min(self.values[len(self.values)-1][1], val))

    def pop(self) -> None:
        del self.values[len(self.values) - 1]

    def top(self) -> int:
        value = self.values[len(self.values) - 1][0]
        return value
        
    def getMin(self) -> int:
        return self.values[len(self.values) - 1][1]