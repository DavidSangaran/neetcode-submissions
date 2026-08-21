class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        getNode = self.head.next
        for _ in range(index):
            getNode = getNode.next
        return getNode.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        getNode = self.head
        while getNode.next:
            getNode = getNode.next
        getNode.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
           return
        getNode = self.head
        for _ in range(index):
            getNode = getNode.next
        newNode = ListNode(val)
        newNode.next = getNode.next
        getNode.next = newNode
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        getNode = self.head
        for _ in range(index):
            getNode = getNode.next
        getNode.next = getNode.next.next
        self.size -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)