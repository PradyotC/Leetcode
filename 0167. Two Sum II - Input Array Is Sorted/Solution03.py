/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.69 %
    Runtime : 329 ms
    Memory Usage : 15.1 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 5.20 % of python3 submissions.
        Your memory usage beats 10.97 % of python3 submissions.
}
*/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1
        dictt = {}
        while numbers:
            k = numbers.pop(0)
            if target-k in dictt: return [dictt[target-k],i]
            if k not in dictt: dictt[k]=i
            # print(numbers,dictt)
            i+=1