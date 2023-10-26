# Time: O(n)
# Space: O(1) 
# delete one duplicate at a time, update left and right pointers
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        left = right = head
        if not head:
            return head
        right = right.next
        while right:
            nxt = right.next
            if left.val == right.val:
                left.next, right = nxt, nxt
            else:
                left, right = left.next, nxt
            
        return head