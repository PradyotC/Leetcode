/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.04 %
    Runtime : 179 ms
    Memory Usage : 18 MB
    Testcase : 10 / 10 passed
    Ranking : 
        Your runtime beats 30.72 % of python3 submissions.
        Your memory usage beats 82.49 % of python3 submissions.
}
*/

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
        

#     def add(self, val: int) -> int:
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# using heap

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.min1 = nums
        self.k = k
        i = len(nums)-self.k
        while i>0:
            heapq.heappop(self.min1)
            i-=1
    def add(self, val: int) -> int:
        if len(self.min1)<self.k: heapq.heappush(self.min1,val) 
        elif val>self.min1[0]:  
            heapq.heappop(self.min1)
            heapq.heappush(self.min1,val)
        return self.min1[0]