class MinStack:
    
    def __init__(self):
        self.original = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.original.append(val)
        if self.min_stk:
            self.min_stk.append(min(self.min_stk[-1], val))
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.original.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.original[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
