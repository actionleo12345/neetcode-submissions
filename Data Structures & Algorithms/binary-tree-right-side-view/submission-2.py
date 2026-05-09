# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque([root])

        while q:
            rightMostNode = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightMostNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightMostNode:
                res.append(rightMostNode.val)
        
        return res