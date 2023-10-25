# Time: O(n)
# Space: O(1) 
# 3 stages, 1. pointers to left and lprev, 2. reverse the parts from left to right, 3. update lprev pointers
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lprev, curr = dummy, head
  
        for i in range(left-1):
            curr = curr.next
            lprev = lprev.next

        prev = None
        for j in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        lprev.next.next = curr
        lprev.next = prev
        return dummy.next
