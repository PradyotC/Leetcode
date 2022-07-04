/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 44.75 %
    Runtime : 75 ms
    Memory Usage : 14 MB
    Testcase : 166 / 166 passed
    Ranking : 
        Your runtime beats 27.21 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        h1 = ListNode(-101,None)
        h2 = ListNode(-101,None)
        h3 = h1
        while head:
            if not head.next:
                if not h2.val == head.val:
                    h3.next = ListNode(head.val,None)
                break
            if head.val == head.next.val:
                h2.next = ListNode(head.val,None)
                h2 = h2.next
            else:
                if not h2.val == head.val:
                    h3.next = ListNode(head.val,None)
                    h3 = h3.next
            head = head.next
            # print(h1,head.val,h3.val)
        return h1.next