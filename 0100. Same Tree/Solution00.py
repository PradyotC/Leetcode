/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.80 %
    Runtime : 60 ms
    Memory Usage : 13.9 MB
    Testcase : 60 / 60 passed
    Ranking : 
        Your runtime beats 16.26 % of python3 submissions.
        Your memory usage beats 75.34 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def same(a,b):
            if not (a or b): return True 
            if a and not b: return False
            if not a and b: return False
            if a.val!=b.val: return False
            return same(a.left,b.left) and same(a.right,b.right)
        
        return same(p,q)
            