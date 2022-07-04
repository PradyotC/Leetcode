/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 74.82 %
    Runtime : 147 ms
    Memory Usage : 17 MB
    Testcase : 35 / 35 passed
    Ranking : 
        Your runtime beats 84.41 % of python3 submissions.
        Your memory usage beats 53.16 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        stack = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                if curr.val<val:
                    curr = None
                    continue
                curr = curr.left
            elif stack:
                curr = stack.pop()
                if curr.val>val: 
                    curr.left = TreeNode(val,left = curr.left) 
                    return root
                curr = curr.right
            else: break
        curr = root
        while curr.right: curr = curr.right
        curr.right = TreeNode(val)
        return root
                
