class Node:
    def __init__(self,data=0,next=None):
        self.val=data
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp=self.head
        while index>0:
            temp=temp.next
            index-=1
        return temp.val
    def addAtHead(self, val: int) -> None:
        newNode=Node(val,self.head)
        self.head=newNode
        self.size+=1

    def addAtTail(self, val: int) -> None:
        temp=self.head
        newNode=Node(val)
        if not self.head:
            self.head = newNode
        else:
            while temp.next:
                temp=temp.next
            temp.next=newNode
        self.size+=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index < self.size:
            newNode=Node(val)
            temp=self.head
            index=index-1
            while index>0:
                temp=temp.next
                index-=1
            tmp=temp.next
            temp.next=newNode
            newNode.next=tmp
            self.size+=1
        elif index == self.size:
            self.addAtTail(val)
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        elif index==0:
            temp=self.head
            self.head=temp.next
            temp.next=None
        else:
            temp=self.head
            index=index-1
            while index>0:
                temp=temp.next
                index-=1
            node = temp.next
            temp.next = node.next
        self.size-=1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)