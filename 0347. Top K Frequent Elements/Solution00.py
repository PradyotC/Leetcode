/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.00 %
    Runtime : 110 ms
    Memory Usage : 18.9 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 90.52 % of python3 submissions.
        Your memory usage beats 34.00 % of python3 submissions.
}
*/

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt,ans = {},{}
        for i in nums: dictt[i] = dictt.get(i,0)+1
        for key,val in dictt.items(): ans[-val] = ans.get(-val,[])+[key]
        ans = list(ans.items())
        heapq.heapify(ans)
        dictt = []
        while ans:
            if len(dictt)>=k: return dictt[:k]
            dictt+=heapq.heappop(ans)[1]
        return dictt[:k]
        
        