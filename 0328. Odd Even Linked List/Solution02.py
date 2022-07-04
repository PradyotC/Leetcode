/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.73 %
    Runtime : 87 ms
    Memory Usage : 16.6 MB
    Testcase : 70 / 70 passed
    Ranking : 
        Your runtime beats 13.94 % of python3 submissions.
        Your memory usage beats 28.63 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        head = ListNode(-1,head)
        prev = head
        h1 = head.next
        evenhead = ListNode(-1)
        even = evenhead
        i = 1
        while h1:
            if i%2==0:
                prev.next = None
                even.next = ListNode(h1.val)
                even = even.next
            else:
                prev.next = h1
                prev = prev.next
            h1 = h1.next
            i+=1
        prev.next = evenhead.next
        return head.next