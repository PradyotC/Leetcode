/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 76.68 %
    Runtime : 155 ms
    Memory Usage : 16.6 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 10.15 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using recursion
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root: return
#         if root.val==val: return root
#         self.ans = None
#         def search(r):
#             if not r: return False
#             if r.val==val: 
#                 self.ans = r
#                 return True
#             if r.val>val and search(r.left): return True
#             if r.val<val and search(r.right): return True
#             return False
#         if search(root.left): return self.ans 
#         search(root.right)
#         return self.ans
        

# using iteration
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:    
        if not root: return
        stack = []
        while True:
            if root:
                if root.val==val: return root
                stack.append(root)
                if root.val<val: 
                    root=None
                    continue
                root = root.left
            elif stack:
                root = stack.pop()
                if root.val==val: return root
                root = root.right
            else: break
        return None
                
            
            
            