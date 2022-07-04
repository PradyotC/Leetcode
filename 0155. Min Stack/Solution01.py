/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 50.81 %
    Runtime : 58 ms
    Memory Usage : 17.9 MB
    Testcase : 31 / 31 passed
    Ranking : 
        Your runtime beats 97.40 % of python3 submissions.
        Your memory usage beats 58.11 % of python3 submissions.
}
*/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if self.stack==[]: self.min.append(val)
        elif self.getMin()>=val: self.min.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack)==1: 
            self.stack=[]
            self.min = []
        elif self.stack!=[]:
            if self.top()==self.getMin(): self.min.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()