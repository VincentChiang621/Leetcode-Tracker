# Time: O(n)
# Space: O(1) 
# make a carry val, go next if there exists is, if not, stay at 0
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        add = 0

        while l1 or l2 or add:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

            total = add + val1 + val2
            add = 1 if total >= 10 else 0
            curr.next = ListNode()
            curr = curr.next
            curr.val = total % 10
        
        return head.next