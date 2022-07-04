/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 56.04 %
    Runtime : 34 ms
    Memory Usage : 14.1 MB
    Testcase : 16 / 16 passed
    Ranking : 
        Your runtime beats 83.41 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class MyStack:

    def __init__(self):
        self.queue,self.q = [],[]

    def push(self, x: int) -> None:
        while self.queue: self.q.append(self.queue.pop(0))
        self.queue.append(x)
        while self.q: self.queue.append(self.q.pop(0)) 

    def pop(self) -> int: return self.queue.pop(0)

    def top(self) -> int: return self.queue[0]        

    def empty(self) -> bool: return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()