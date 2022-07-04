/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 64.98 %
    Runtime : 61 ms
    Memory Usage : 13.9 MB
    Testcase : 68 / 68 passed
    Ranking : 
        Your runtime beats 13.91 % of python3 submissions.
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]