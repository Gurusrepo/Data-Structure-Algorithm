# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        temp = ListNode(-1,head)
        currNode = temp
        nextNode = temp

        for i in range(n+1):
            nextNode = nextNode.next
        

        while nextNode:
            currNode = currNode.next
            nextNode = nextNode.next
        
        currNode.next = currNode.next.next


        return temp.next

        

        
        


        

        