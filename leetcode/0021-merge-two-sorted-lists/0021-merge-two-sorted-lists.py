# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        self.res = ListNode(-1)
        self.dummy = self.res 

        while list1 and list2 :

            if list1.val < list2.val :
                self.res.next = list1
                list1 = list1.next 
            
            else :
                self.res.next = list2
                list2 = list2.next 

            self.res = self.res.next 

        self.res.next = list1 or list2 

        return self.dummy.next 
        