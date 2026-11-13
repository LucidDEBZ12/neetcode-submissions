
class Solution:
    def goodNodes(self, root):

        if not root:
            return 0

        stack = [(root, root.val)]

        good = 0

        while stack:

            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                good += 1

            max_so_far = max(max_so_far, node.val)

            if node.right:
                stack.append((node.right, max_so_far))

            if node.left:
                stack.append((node.left, max_so_far))

        return good
