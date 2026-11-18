# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:

        slow = head 
        fast = head 

        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
        
        
        prev = None
        middle = slow.next  # second half
        slow.next = None  # break the second half

        while middle :
            revNode = ListNode(middle.val)
            revNode.next = prev 
            prev = revNode
            middle =  middle.next 

        firstpart = head 
        secondpart = prev 
        
        while secondpart :
            firstNext = firstpart.next 
            secondNext = secondpart.next 

            firstpart.next = secondpart 
            secondpart.next = firstNext 

            firstpart = firstNext 
            secondpart = secondNext 
        
        return head
         
        



        