/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 45.98 %
    Runtime : 53 ms
    Memory Usage : 15.2 MB
    Testcase : 117 / 117 passed
    Ranking : 
        Your runtime beats 74.01 % of python3 submissions.
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not (root.left or root.right): return root.val==targetSum
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
        