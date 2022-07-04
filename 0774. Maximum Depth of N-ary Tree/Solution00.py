/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.27 %
    Runtime : 96 ms
    Memory Usage : 16 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 9.18 % of python3 submissions.
        Your memory usage beats 52.67 % of python3 submissions.
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