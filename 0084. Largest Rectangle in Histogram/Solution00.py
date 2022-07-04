/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 41.25 %
    Runtime : 1768 ms
    Memory Usage : 30.4 MB
    Testcase : 98 / 98 passed
    Ranking : 
        Your runtime beats 25.49 % of python3 submissions.
        Your memory usage beats 29.50 % of python3 submissions.
}
*/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
            
        for start,h in stack:
            maxArea = max(maxArea, h*(len(heights) - start))
            
        return maxArea