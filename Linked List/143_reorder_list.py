# Time: O(n)
# Space: O(1)
# 1. reverse second half of node List; 2. reorder and update pointers
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev, nxt = None, None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # start the alg
        while head != prev:
            nxt = head.next
            head.next = prev
            head = nxt
            if head != prev:
                nxt = prev.next
                prev.next = head
                prev = nxt

        return head