# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False

    #     if self.isSameTree(root, subRoot):
    #         return True

    #     return (self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot))


    # def isSameTree(self, r, s):
    #     if not r and not s:
    #         return True
        
    #     if r and s and r.val == s.val:
    #         return (self.isSameTree(r.left, s.left) and 
    #                 self.isSameTree(r.right, s.right))
        
    #     return False

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        # if not p or not q or p.val != q.val:
        #     return False
        # return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))