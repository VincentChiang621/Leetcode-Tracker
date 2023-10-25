# Time: O(n + m)
# Space: O(1) 
# find out length, let the longer one start at the difference, then check each time if they are equal
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        alen = blen = 0
        starta, startb = headA, headB

        while starta:
            alen += 1
            starta = starta.next
        
        while startb:
            blen += 1
            startb = startb.next

        while alen > blen:
            alen -= 1
            headA = headA.next
        
        while blen > alen:
            blen -= 1
            headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None