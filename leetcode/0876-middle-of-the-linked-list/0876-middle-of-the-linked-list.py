# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        fast = head 
        

        while fast and fast.next :
            head = head.next
            fast = fast.next.next 
        
        return head
            
            


        # length = 0 
        # temp = head 

        # while temp:
        #     temp = temp.next 
        #     length += 1
        
        
        # mid = (length // 2) + 1 
        
        # count = 0
        # while head :
        #     count += 1 
        #     if mid == count :
        #         return head
        #     head = head.next 
        