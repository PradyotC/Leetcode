/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 76.37 %
    Runtime : 56 ms
    Memory Usage : 16.4 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 87.43 % of python3 submissions.
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        if not root.children: return [root.val]
        ret = [root.val]
        for i in root.children:
            ret+=self.preorder(i)
        return ret
        
        