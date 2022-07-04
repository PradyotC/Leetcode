/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 48.79 %
    Runtime : 9771 ms
    Memory Usage : 15.2 MB
    Testcase : 57 / 57 passed
    Ranking : 
        Your memory usage beats 24.25 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = range(len(nums))
        dictt = {i:nums[i] for i in a}
        for i in a:
            for k,v in dictt.items():
                if v==target-nums[i]:
                    ans = list(set([i,k]))
                    if len(ans)==2:
                        return ans
                # return [k]
#         for i in dictt.keys():
#             j = target-nums[i]
#             print(dictt,j)
#             if j in dictt.values:
                
#                 return [i,d2[j]]
            