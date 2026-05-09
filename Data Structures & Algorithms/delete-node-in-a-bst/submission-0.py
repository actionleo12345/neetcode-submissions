# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        cur = root
        left = root.left
        right = root.right
        # find the smallest node under the right node(cur node's right child), which is going to the right node then go down to the left layer-by-layer until we get the leftmsot node, which is the smallest node under the right node(cur node's right child).
        while right.left:
            right = right.left
        right.left = left
        return cur.right
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            return self.helper(root)

        cur = root
        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                root = root.right
        
        return cur