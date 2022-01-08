class MyCircularDeque:

    def __init__(self, k: int):
        self.que=[]
        self.max=k
        

    def insertFront(self, value: int) -> bool:
        if len(self.que)==[]:
            self.que.append(value)
            return True
        elif len(self.que)<self.max:
            self.que.insert(0,value)
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.que)==[] or len(self.que)<self.max:
            self.que.append(value)
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if len(self.que)==0:
            return False
        else:
            self.que.pop(0)
            return True
        

    def deleteLast(self) -> bool:
        if len(self.que)==0:
            return False
        else:
            self.que.pop()
            return True
        
    def getFront(self) -> int:
        if self.que==[]:
            return -1
        return self.que[0]
        

    def getRear(self) -> int:
        if self.que==[]:
            return -1
        return self.que[-1]
        

    def isEmpty(self) -> bool:
        if self.que ==[]:
            return True
        return False
        

    def isFull(self) -> bool:
        if len(self.que)==self.max:
            return True
        return False
