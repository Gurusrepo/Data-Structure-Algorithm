# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1 = headA
        list2 = headB 

        while list1 != list2 : 
     
            if not list1 :
                list1 = headB
            else :
                list1 = list1.next  
             
            if not list2 :
                list2 = headA
            else:
                list2 = list2.next
        
        return list1 #return any list


        