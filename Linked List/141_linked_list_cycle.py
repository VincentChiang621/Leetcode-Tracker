# Time: O(n)
# Space: O(1) 
# fast and slow pointer
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        l = r = head

        while r and r.next:
            r = r.next.next
            l = l.next
            if r == l:
                return True
        
        return False