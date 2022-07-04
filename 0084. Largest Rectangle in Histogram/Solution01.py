/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 41.25 %
    Runtime : 997 ms
    Memory Usage : 30.7 MB
    Testcase : 98 / 98 passed
    Ranking : 
        Your runtime beats 96.10 % of python3 submissions.
        Your memory usage beats 23.80 % of python3 submissions.
}
*/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights.append(0)
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