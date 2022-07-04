/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.80 %
    Runtime : 116 ms
    Memory Usage : 14.6 MB
    Testcase : 58 / 58 passed
    Ranking : 
        Your runtime beats 35.96 % of python3 submissions.
        Your memory usage beats 57.93 % of python3 submissions.
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
        # print("enqueue",self.q,self.head,self.tail)
        return True

    def deQueue(self) -> bool:
        if self.head == -1: return False
        if self.q[self.head] == None: return False
        self.q[self.head] = None
        if self.head==self.tail: self.head=self.tail=-1
        else: self.head=(self.head+1)%self.size
        # print("dequeue",self.q,self.head,self.tail)
        return True
        
    def Front(self) -> int:
        # print("front",self.q,self.head,self.tail)
        if self.head == -1: return -1
        return self.q[self.head]

    def Rear(self) -> int:
        # print("rear",self.q,self.head,self.tail)
        if self.tail == -1: return -1
        return self.q[self.tail]
        

    def isEmpty(self) -> bool:
        # print("isEmpty",self.q,self.head,self.tail)
        if self.head==-1: return True
        return False

    def isFull(self) -> bool:
        # print("isFull",self.q,self.head,self.tail)
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