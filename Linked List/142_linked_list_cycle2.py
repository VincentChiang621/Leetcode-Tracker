# Time: O(n)
# Space: O(1) 
# first figure out if there is cycle, if there is move fast ptr to head and 
# update make it go same speed as slow
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle = True
                break
            
        fast = head
        while cycle:
            if fast == slow:
                return fast
            slow = slow.next
            fast = fast.next
            
            
        return None