/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.27 %
    Runtime : 56 ms
    Memory Usage : 16.4 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 75.54 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        m = 0
        [m := max(m,self.maxDepth(i)) for i in root.children]
        return m+1