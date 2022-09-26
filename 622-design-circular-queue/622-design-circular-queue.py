class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.length = k
        self.front = 0
        self.rear = 0
        self.items = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.queue[self.rear % self.length] = value
            self.items += 1
            return True
        if self.queue[(self.rear + 1) % self.length] < 0:
            self.rear += 1
            self.items += 1
            self.queue[self.rear % self.length] = value
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.items == 1:
            self.queue[self.front % self.length] = -1
            self.items -= 1
            return True
            
        if self.queue[self.front % self.length] >= 0:
            self.items -= 1
            self.queue[self.front % self.length] = -1
            self.front += 1
            return True
        return False

    def Front(self) -> int:
        return self.queue[self.front % self.length]

    def Rear(self) -> int:
        return self.queue[self.rear % self.length]
        

    def isEmpty(self) -> bool:
        return self.items == 0
        

    def isFull(self) -> bool:
        return self.items == self.length
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()