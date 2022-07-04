/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.05 %
    Runtime : 42 ms
    Memory Usage : 13.9 MB
    Testcase : 198 / 198 passed
    Ranking : 
        Your runtime beats 76.19 % of python3 submissions.
        Your memory usage beats 93.86 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(p,q):
            if not p and not q:return True
            if p and not q:return False
            if q and not p:return False
            left_answer =symmetric(p.left,q.right) 
            right_answer = symmetric(p.right,q.left)
            return p.val == q.val and left_answer and right_answer
        return symmetric(root,root)