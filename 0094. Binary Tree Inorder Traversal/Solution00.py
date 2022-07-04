/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.37 %
    Runtime : 51 ms
    Memory Usage : 13.9 MB
    Testcase : 70 / 70 passed
    Ranking : 
        Your runtime beats 37.01 % of python3 submissions.
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)