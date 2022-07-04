/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 54.18 %
    Runtime : 273 ms
    Memory Usage : 20.1 MB
    Testcase : 52 / 52 passed
    Ranking : 
        Your runtime beats 56.67 % of python3 submissions.
        Your memory usage beats 91.47 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "None"
        def ser(r):
            ret = ""
            r1 = ""
            if not r.left: 
                ret+=",None"
            else:
                ret+=","+str(r.left.val)
                r1+=ser(r.left)
            if not r.right: 
                ret+=",None"
            else:
                ret+=","+str(r.right.val)
                r1+=ser(r.right)
            return ret+r1
        return str(root.val)+ser(root).rstrip(",None")
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None": return None
        if data.isnumeric(): return TreeNode(int(data))
        self.data = data.split(",")
        ans = TreeNode(int(self.data.pop(0)))
        def des(r):
            if not self.data: return 
            left = self.data.pop(0)
            if self.data: right = self.data.pop(0)
            else: right='None'
            if left!='None': 
                r.left = TreeNode(int(left))
                des(r.left)
            if right!='None': 
                r.right = TreeNode(int(right))
                des(r.right)
        des(ans)
        return ans
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))