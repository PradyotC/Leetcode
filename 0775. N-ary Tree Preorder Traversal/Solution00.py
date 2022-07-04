/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 76.37 %
    Runtime : 87 ms
    Memory Usage : 16.2 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 34.86 % of python3 submissions.
        Your memory usage beats 65.59 % of python3 submissions.
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
        # ret = [root.val]
        # for i in root.children:
        #     ret+=self.preorder(i)
        # return ret
        stack = [root,]
        output = []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
            
        return output
            
        
        
        
        
        
        