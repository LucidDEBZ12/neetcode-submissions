# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val

            summ = l1_val + l2_val + carry
            carry = summ // 10
            digit = summ % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next