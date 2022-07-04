/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.69 %
    Runtime : 193 ms
    Memory Usage : 15.1 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 52.78 % of python3 submissions.
        Your memory usage beats 10.97 % of python3 submissions.
}
*/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i = len(numbers)
        # dictt = {}
        # while numbers:
        #     k = numbers.pop()
        #     if target-k in dictt: return [i,dictt[target-k]]
        #     if k not in dictt: dictt[k]=i
        #     # print(numbers,dictt)
        #     i-=1
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [i+1, j+1]