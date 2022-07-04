/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.80 %
    Runtime : 65 ms
    Memory Usage : 14.7 MB
    Testcase : 58 / 58 passed
    Ranking : 
        Your runtime beats 98.58 % of python3 submissions.
        Your memory usage beats 22.51 % of python3 submissions.
}
*/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None for i in range(k)]
        self.head = -1
        self.tail = -1
        self.size = k
        # print("init",self.q,self.head,self.tail)

    def enQueue(self, value: int) -> bool:
        if self.head == -1: self.head = 0
        if self.q[(self.tail+1)%self.size]!=None: return False
        self.tail = (self.tail+1)%self.size
        self.q[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.head == -1: return False
        if self.q[self.head] == None: return False
        self.q[self.head] = None
        if self.head==self.tail: self.head=self.tail=-1
        else: self.head=(self.head+1)%self.size
        return True
        
    def Front(self) -> int:
        if self.head == -1: return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.tail == -1: return -1
        return self.q[self.tail]
        

    def isEmpty(self) -> bool:
        if self.head==-1: return True
        return False

    def isFull(self) -> bool:
        if (self.tail+1)%self.size==self.head: return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()