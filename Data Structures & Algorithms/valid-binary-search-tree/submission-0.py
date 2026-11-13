
class Solution:
    def isValidBST(self, root):

        def is_valid(node, minn, maxx):

            # Base case
            if not node:
                return True

            # Check whether node violates its boundaries
            if node.val <= minn or node.val >= maxx:
                return False

            # Check both subtrees with updated boundaries
            return (
                is_valid(node.left, minn, node.val)
                and
                is_valid(node.right, node.val, maxx)
            )

        # Start with unlimited boundaries
        return is_valid(root, float('-inf'), float('inf'))
