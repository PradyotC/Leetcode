/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 51.81 %
    Runtime : 165 ms
    Memory Usage : 30.3 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 92.02 % of python3 submissions.
        Your memory usage beats 6.03 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if (not headA) or (not headB): return None
        sett = set()
        while headB:
            if headB not in sett:
                sett.add(headB)
            headB = headB.next
        while headA:
            if headA in sett:
                return headA
            headA = headA.next
        return None
        