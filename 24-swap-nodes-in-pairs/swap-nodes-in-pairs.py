# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the swapping process
        dummy = ListNode(0)
        dummy.next = head
        
        # This will point to the last node of the previous pair
        prev = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move the pointers forward for the next swap
            prev = first
            head = first.next
        
        return dummy.next
