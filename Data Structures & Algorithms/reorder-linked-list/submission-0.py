# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr = slow.next
        slow.next = None #Splits the list
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        print("HERE")
        
        first = head
        while prev:
            temp1, temp2 = first.next, prev.next
            first.next = prev
            prev.next = temp1
            first = temp1
            prev = temp2

        


            
        
        