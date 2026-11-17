# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        low = ListNode(-1)
        high = ListNode(-1) 
        lhead = low
        hhead = high

        while head :
            if head.val < x :
                lhead.next = head
                lhead = lhead.next

            else :
                hhead.next = head
                hhead = hhead.next  
            
            head = head.next 
        
        hhead.next = None 
        lhead.next = high.next 

        return low.next
        
        