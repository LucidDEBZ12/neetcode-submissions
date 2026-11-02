class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head
        old_to_new = {}

        # PASS 1: Create a copy of every node
        while curr:
            node = Node(x=curr.val)
            old_to_new[curr] = node
            curr = curr.next

        # PASS 2: Connect next and random pointers
        curr = head

        while curr:
            new_node = old_to_new[curr]

            new_node.next = (
                old_to_new[curr.next] if curr.next else None
            )

            new_node.random = (
                old_to_new[curr.random] if curr.random else None
            )

            curr = curr.next

        return old_to_new[head]   