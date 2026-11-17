# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        if not head or not head.next :
            return head
        
        prev = ListNode(0)
        dummy = prev 

        firstNode = head 
        secondNode = head.next 

        while firstNode and secondNode :
            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode 
            prev = firstNode

            firstNode = prev.next  

            if firstNode :
                secondNode = firstNode.next
        
        
        return dummy.next

        