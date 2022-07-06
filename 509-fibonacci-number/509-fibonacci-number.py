class Solution:
    def __init__(self):
        self.dictt = {
            0:0,
            1:1
        }
    def fib(self, n: int) -> int:
        if n in self.dictt: return self.dictt[n]
        self.dictt[n] = self.fib(n-1)+self.fib(n-2)
        return self.dictt[n]