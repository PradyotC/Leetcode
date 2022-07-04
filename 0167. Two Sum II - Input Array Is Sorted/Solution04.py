/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.69 %
    Runtime : 197 ms
    Memory Usage : 14.9 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 50.46 % of python3 submissions.
        Your memory usage beats 41.26 % of python3 submissions.
}
*/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = len(numbers)
        dictt = {}
        while numbers:
            k = numbers.pop()
            if target-k in dictt: return [i,dictt[target-k]]
            if k not in dictt: dictt[k]=i
            # print(numbers,dictt)
            i-=1