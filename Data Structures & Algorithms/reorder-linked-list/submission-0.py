# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #finding the middle element
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nextnode = second.next
            second.next = prev
            prev = second
            second = nextnode
        
        #merging alternative elements
        first = head
        last = prev
        while last:
            firstnext=first.next
            lastnext = last.next
            first.next = last
            last.next=firstnext
            first=firstnext
            last=lastnext