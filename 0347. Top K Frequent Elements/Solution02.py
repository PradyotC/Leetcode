/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.00 %
    Runtime : 132 ms
    Memory Usage : 18.7 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 69.83 % of python3 submissions.
        Your memory usage beats 46.82 % of python3 submissions.
}
*/

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        for i in nums: dictt[i] = dictt.get(i,0)+1
        ans = {}
        for key,val in dictt.items(): ans[-val] = ans.get(-val,[])+[key]
        # print(ans)
        ans = list(ans.items())
        heapq.heapify(ans)
        # print(ans)
        dictt = []
        while ans:
            if len(dictt)>=k: return dictt[:k]
            dictt+=heapq.heappop(ans)[1]
        return dictt[:k]
        
        