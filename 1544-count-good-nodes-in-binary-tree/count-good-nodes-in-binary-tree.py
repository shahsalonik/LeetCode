# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, curr_max):
            if not node:
                return 0

            if node.val >= curr_max:
                good = 1
            else:
                good = 0
            
            new_max = max(node.val, curr_max)
            
            return good + helper(node.left, new_max) + helper(node.right, new_max)

        return helper(root, root.val)