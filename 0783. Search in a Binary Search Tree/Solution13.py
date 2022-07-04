/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 76.68 %
    Runtime : 85 ms
    Memory Usage : 16.6 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 84.01 % of python3 submissions.
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return
        if root.val==val: return root
        self.ans = None
        def search(r,v):
            if not r: return
            if r.val==v: 
                self.ans = r
                return
            if r.left: search(r.left,v)
            if r.right: search(r.right,v)
            return
        search(root,val)
        return self.ans
            
            
            