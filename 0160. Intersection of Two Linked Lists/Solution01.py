/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 51.81 %
    Runtime : 158 ms
    Memory Usage : 30.4 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 96.91 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
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
        # if (not headA.next) or (not headB.next): return 0
        # h1 = headA
        # h2 = None
        # while h1:
        #     h2 = ListNode(h1.val,h2)
        #     h1 = h1.next
        # h3 = headB
        # h4 = None
        # while h3:
        #     h4 = ListNode(h3.val,h4)
        #     h3 = h3.next
        # ans = None
        # while h2 or h4:
        #     if h2.val!=h4.val:
        #         break
        #     ans = ListNode(h2.val,ans)
        #     h2 = h2.next
        #     h4 = h4.next
        # return ans
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
        