/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 67.87 %
    Runtime : 90 ms
    Memory Usage : 19.7 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 73.99 % of python3 submissions.
        Your memory usage beats 99.85 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Here we have used inorder traversal using stack
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ans = []
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                self.ans.append(root.val)
                root = root.right
            else: break

    def next(self) -> int: return self.ans.pop(0)
        
    def hasNext(self) -> bool: return bool(self.ans)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()