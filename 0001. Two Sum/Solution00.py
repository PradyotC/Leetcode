/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 48.79 %
    Runtime : 122 ms
    Memory Usage : 15.5 MB
    Testcase : 57 / 57 passed
    Ranking : 
        Your runtime beats 43.21 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution(object):
    def twoSum(self, nums, target):
        buffer_dictionary = {}
        for i in range(nums.__len__()):
            if nums[i] in buffer_dictionary:
                return [buffer_dictionary[nums[i]], i]
            buffer_dictionary[target - nums[i]] = i