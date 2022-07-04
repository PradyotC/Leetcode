/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 49.34 %
    Runtime : 99 ms
    Memory Usage : 18.4 MB
    Testcase : 91 / 91 passed
    Ranking : 
        Your runtime beats 65.33 % of python3 submissions.
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return
        def delete(node):
            if not (node.left or node.right): return None
            if not node.right: return node.left
            if not node.left: return node.right
            n = node.left
            while n.right: n = n.right
            n.right = node.right
            return node.left
        if root.val==key: return delete(root)
        stack = []
        curr = root
        while True:
            if curr:
                if curr.left and curr.left.val==key:
                    curr.left=delete(curr.left)
                    return root
                stack.append(curr)
                if curr.val<key:
                    curr = None
                    continue
                curr = curr.left
            elif stack:
                curr = stack.pop()
                if curr.right and curr.right.val==key:
                    curr.right=delete(curr.right)
                    return root
                curr = curr.right
            else: break
        return root