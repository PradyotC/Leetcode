class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        ans = [0,1]
        while n>2:
            ans.insert(1,ans.pop(0))
            ans[1] = sum(ans)
            n-=1
        return sum(ans)