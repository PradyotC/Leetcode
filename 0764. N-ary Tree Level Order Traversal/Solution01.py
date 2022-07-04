/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 69.03 %
    Runtime : 109 ms
    Memory Usage : 16 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 10.37 % of python3 submissions.
        Your memory usage beats 51.33 % of python3 submissions.
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
    def levelOrder(self, root: 'Node') -> List[List[int]]: 
        if not root: return []
        def depth(r):
            if not r: return 0
            m = 0
            for i in r.children:
                m = max(m,depth(i))
            return 1+m
        ret  = [[] for i in range(depth(root))]
        if ret==[[]]: return [[root.val]]
        def dth(r,d):
            if not r: return None
            ret[d] += [r.val]
            for i in r.children:
                dth(i,d+1)
        dth(root,0)
        return ret
                
        