/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 41.25 %
    Runtime : 1693 ms
    Memory Usage : 31.4 MB
    Testcase : 98 / 98 passed
    Ranking : 
        Your runtime beats 30.81 % of python3 submissions.
        Your memory usage beats 17.19 % of python3 submissions.
}
*/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
            
        return maxArea