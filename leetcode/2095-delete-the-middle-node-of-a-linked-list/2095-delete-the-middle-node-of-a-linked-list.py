# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:

        if not head or not head.next :
            return None
        
        prev = ListNode(1)
        dummy = prev
        slow = head 
        fast = head

        while fast and fast.next :
            prev.next = slow
            prev = prev.next
            slow = slow.next 
            fast = fast.next.next 

        
        prev.next = prev.next.next
        return dummy.next

        