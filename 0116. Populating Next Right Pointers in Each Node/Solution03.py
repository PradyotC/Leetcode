/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 58.00 %
    Runtime : 176 ms
    Memory Usage : 15.5 MB
    Testcase : 59 / 59 passed
    Ranking : 
        Your runtime beats 5.04 % of python3 submissions.
        Your memory usage beats 75.07 % of python3 submissions.
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        if not (root.left or root.right): return root
        def conn(p,q):
            if not (p or q): return
            p.next = q
            conn(p.left,p.right)
            conn(q.left,q.right)
            if p.right and q.left:
                conn(p.right,q.left)
            return
        conn(root.left,root.right)
        return root
        