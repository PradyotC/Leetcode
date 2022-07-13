class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        score = nums[0]
        dq.append((0,score))
        for i in range(1,n):
            while dq and dq[0][0] < i-k:
                dq.popleft()
            score = nums[i]+dq[0][1]
            while dq and dq[-1][1] <= score:
                dq.pop()
            dq.append((i,score))
        return score