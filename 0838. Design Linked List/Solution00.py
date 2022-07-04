/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 27.14 %
    Runtime : 396 ms
    Memory Usage : 15.6 MB
    Testcase : 64 / 64 passed
    Ranking : 
        Your runtime beats 17.97 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class MyLinkedList:

    def __init__(self):
        self.val = -1
        self.next = None
        self.head = self

    def get(self, index: int) -> int:
        h1 = self.head
        i=0
        while h1:
            if i==index:
                return h1.val
            i+=1
            h1 = h1.next
        return -1

    def addAtHead(self, val: int) -> None:
        h1 = MyLinkedList()
        h1.val = val
        if self.head and self.head.val!=-1:
            h1.next = self.head
        self.head = h1
        
    def addAtTail(self, val: int) -> None:
        data = MyLinkedList()
        data.val = val
        if self.head.val==-1: 
            self.head = data
        else:
            h1 = self.head
            # h1 = self
            while h1.next:
                h1 = h1.next
            h1.next = data

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            h1 = MyLinkedList()
            h1.val = val
            h1.next = self.head
            self.head = h1
        else:
            prev = self.head
            h1 = prev.next
            i = 1
            c = True
            while h1:
                if i==index:
                    h2 = MyLinkedList()
                    h2.val = val
                    h2.next = h1
                    prev.next = h2
                    c = False
                    break
                prev = h1
                h1 = h1.next
                i+=1
            if i==index and c:
                h2 = MyLinkedList()
                h2.val = val
                prev.next = h2

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.head = self.head.next
        else:
            prev = self.head
            h1 = prev.next
            i = 1
            while h1:
                if i==index:
                    prev.next = h1.next
                    break
                prev = h1
                h1 = h1.next
                i+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)