# Time: O(n)
# Space: O(1) 
# slow and fast, reverse second half, then go change
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp


        while head and prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True