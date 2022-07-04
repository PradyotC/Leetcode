/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 43.70 %
    Runtime : 36 ms
    Memory Usage : 14.1 MB
    Testcase : 44 / 44 passed
    Ranking : 
        Your runtime beats 83.11 % of python3 submissions.
        Your memory usage beats 18.43 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        strt = ListNode()
        s1 = strt
        ans = ListNode(-501)
        cntr = 1
        op = 0
        while head:
            if cntr < left:
                strt.next = ListNode(head.val)
                strt = strt.next
            if cntr == left:
                op = 1
            if op == 1:
                ans = ListNode(head.val,ans)
            if cntr == right:
                op = 0
                break
            cntr += 1
            head = head.next
        # print(s1.next)
        # print(strt)
        # print(ans)
        # print(head.next)
        while ans and ans.next:
            strt.next = ListNode(ans.val)
            strt = strt.next
            if ans.next.val==-501:
                break
            ans = ans.next
        strt.next = head.next
        # print(s1.next)
        return s1.next
        