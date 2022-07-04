/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.02 %
    Runtime : 41 ms
    Memory Usage : 16.1 MB
    Testcase : 28 / 28 passed
    Ranking : 
        Your runtime beats 84.68 % of python3 submissions.
        Your memory usage beats 24.83 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        ans = None
        while head:
            ans = ListNode(head.val,ans)
            head = head.next
        return ans
        