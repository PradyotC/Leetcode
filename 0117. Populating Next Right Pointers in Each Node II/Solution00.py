/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.79 %
    Runtime : 57 ms
    Memory Usage : 15.5 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your runtime beats 76.71 % of python3 submissions.
        Your memory usage beats 12.99 % of python3 submissions.
}
*/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        if not (root.left or root.right): return root
        self.ans = {}
        def fill(r,d):
            if not r: return
            if d in self.ans:
                self.ans[d].next = r
            self.ans[d] = r    
            if r.left: fill(r.left,d+1)
            if r.right: fill(r.right,d+1)
            return
        fill(root,0)
        return root
    
    
    def maxDepth(self, root) -> int:
        if not root: return 0
        if not (root.left or root.right): return 1
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))