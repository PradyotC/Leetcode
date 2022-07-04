/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 72.31 %
    Runtime : 87 ms
    Memory Usage : 16.5 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 10.08 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not (root.left or root.right): return 1
        self.ans=1
        def lvl(r,d):
            if not r: return
            self.ans = max(self.ans,d)
            lvl(r.left,d+1)
            lvl(r.right,d+1)
        lvl(root,1)
        return self.ans