# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        headNode = prevNode = min(list1, list2, key=lambda x: x.val)
        
        if headNode is list1:
            list1 = list1.next
        else:
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                prevNode.next = list1
                list1 = list1.next
            else:
                prevNode.next = list2
                list2 = list2.next
            prevNode = prevNode.next

        prevNode.next = list1 if list1 else list2

        return headNode
            

            
        