# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        
        oddNode = ListNode(-1)  
        evenNode = ListNode(-1) 
        dummyodd = oddNode 
        dummyeven = evenNode

        count = 1

        while head :
            if count % 2 != 0 :
                oddNode.next = head
                oddNode = oddNode.next
            else :
                evenNode.next = head
                evenNode = evenNode.next

            head = head.next
            count += 1 
        

        evenNode.next = None 
        oddNode.next = dummyeven.next
        
        
        return dummyodd.next


        