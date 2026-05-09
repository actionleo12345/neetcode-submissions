# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        stack = []
        cur_node = root

        while cur_node or stack:
            # to the bottom leftmost node
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop()
            cnt += 1
            if cnt == k:
                return cur_node.val
            # move to the right of the cur_node
            cur_node = cur_node.right