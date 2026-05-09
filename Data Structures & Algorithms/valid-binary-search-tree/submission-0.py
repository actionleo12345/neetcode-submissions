# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validation(root, left_bound, right_bound):
            if not root:
                return True
            
            if not (left_bound < root.val < right_bound):
                return False

            return (validation(root.left, left_bound, root.val) and 
                    validation(root.right, root.val, right_bound))
        
        return validation(root, float('-inf'), float('inf'))