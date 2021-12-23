class MyQueue:

    def __init__(self):
        self.queue=[]
        self.leng=0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.leng+=1
    def pop(self) -> int:
        self.leng-=1
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.leng==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
