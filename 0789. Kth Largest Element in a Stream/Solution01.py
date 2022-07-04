/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.04 %
    Runtime : 180 ms
    Memory Usage : 18.3 MB
    Testcase : 10 / 10 passed
    Ranking : 
        Your runtime beats 29.98 % of python3 submissions.
        Your memory usage beats 48.44 % of python3 submissions.
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
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]