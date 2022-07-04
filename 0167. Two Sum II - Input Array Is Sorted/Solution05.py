/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.69 %
    Runtime : 144 ms
    Memory Usage : 15 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 82.23 % of python3 submissions.
        Your memory usage beats 10.97 % of python3 submissions.
}
*/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = len(numbers)
        dictt = {}
        while i>0:
            k = numbers.pop()
            if target-k in dictt: return [i,dictt[target-k]]
            if k not in dictt: dictt[k]=i
            # print(numbers,dictt)
            i-=1