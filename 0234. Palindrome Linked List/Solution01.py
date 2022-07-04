/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 47.29 %
    Runtime : 2539 ms
    Memory Usage : 47 MB
    Testcase : 86 / 86 passed
    Ranking : 
        Your memory usage beats 21.57 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
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
        rev = None
        h1 = head
        while h1:
            rev = ListNode(h1.val,rev)
            h1 = h1.next
        while head and rev:
            if head.val!=rev.val: return False
            head,rev = head.next,rev.next
        return True