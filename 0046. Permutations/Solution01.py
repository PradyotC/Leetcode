/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 73.17 %
    Runtime : 63 ms
    Memory Usage : 14.2 MB
    Testcase : 26 / 26 passed
    Ranking : 
        Your runtime beats 45.02 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def per(arr,ans):
            if not arr:
                self.ans.append(ans)
                return
            for i in arr:
                arr1 = arr.copy()
                ans1 = ans+[i]
                arr1.remove(i)
                per(arr1,ans1)
        per(nums.copy(),[])
        return self.ans