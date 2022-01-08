class MinStack:

    def __init__(self):
        self.stak=[]
        self.minn=[]

    def push(self, val: int) -> None:
        self.stak.append(val)
        if self.minn == []:
            self.minn.append(val)
        elif val <= self.minn[-1]:
            self.minn.append(val)

    def pop(self) -> None:
        if self.stak[-1] == self.minn[-1]:
            self.minn.pop()
        self.stak.pop()

    def top(self) -> int:
        return self.stak[-1]

    def getMin(self) -> int:
        if self.minn != []:
            return self.minn[-1]
        else:
            return None
