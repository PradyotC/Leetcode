/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.27 %
    Runtime : 47 ms
    Memory Usage : 16 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 93.22 % of python3 submissions.
        Your memory usage beats 93.31 % of python3 submissions.
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
        if not root.children: return 1
        for i in range(len(root.children)):
            root.children[i] = self.maxDepth(root.children[i])
        return max(root.children)+1