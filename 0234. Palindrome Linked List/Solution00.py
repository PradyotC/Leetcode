/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 47.29 %
    Runtime : 1579 ms
    Memory Usage : 47.2 MB
    Testcase : 86 / 86 passed
    Ranking : 
        Your runtime beats 10.74 % of python3 submissions.
        Your memory usage beats 10.53 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        if not head.next: return True
        # rev = None
        s = ""
        h1 = head
        while h1:
            # rev = ListNode(h1.val,rev)
            s+=str(h1.val)
            h1 = h1.next
        return s==s[::-1]
        # while head and rev:
        #     if head.val!=rev.val: return False
        #     head,rev = head.next,rev.next
        # return True