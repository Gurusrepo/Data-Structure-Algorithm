# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        
        temp = None
        tempHead = head 

        while tempHead :
            newNode = ListNode(tempHead.val)
            nextNode = newNode.next 
            newNode.next = temp 
            temp = newNode
            tempHead = tempHead.next
        
        last = temp
        first = head


        while first :
            if first.val != last.val :
                return False 
            else :
                first = first.next 
                last = last.next 
        
        return True
        