# Time: O(n)
# Space: O(1) 
# keep a dummy node, keep r in n-distance from l and remove the node
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        l, r = dummy, head

        for i in range(n):
            r = r.next

        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return dummy.next