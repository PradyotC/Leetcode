/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 59.35 %
    Runtime : 51 ms
    Memory Usage : 13.9 MB
    Testcase : 22 / 22 passed
    Ranking : 
        Your runtime beats 33.76 % of python3 submissions.
        Your memory usage beats 98.28 % of python3 submissions.
}
*/

class MyQueue:

    def __init__(self):
        self.stack,self.s = [],[]
        
    def push(self, x: int) -> None:
        while self.stack: self.s.append(self.stack.pop())    
        self.stack.append(x)
        while self.s: self.stack.append(self.s.pop())

    def pop(self) -> int: return self.stack.pop()
        
    def peek(self) -> int: return self.stack[-1]

    def empty(self) -> bool: return not self.stack
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()