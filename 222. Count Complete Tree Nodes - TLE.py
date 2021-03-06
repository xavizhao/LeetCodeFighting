'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.count = 0
        self.traversal(root)
        return self.count

    def traversal(self, root):
        self.count += 1
        if root.left is not None:
            self.traversal(root.left)
        if root.right is not None:
            self.traversal(root.right)

mySolution = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(8)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
re = mySolution.countNodes(root)
print(re)