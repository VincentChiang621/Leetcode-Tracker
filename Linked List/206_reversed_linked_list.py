# Time: O(N)
# Space: O(1) 
# prev and curr pointers update as needed
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next1 = head
        prev = None

        while next1:
            next1 = next1.next
            head.next = prev
            prev = head
            head = next1

        return prev
            