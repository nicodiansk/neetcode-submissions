# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        
        while q:
            
            
            current = []
            lenQ = len(q)
            for i in range(lenQ):
                node = q.popleft()
                current.append(node.val)
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
            if current:
                res.append(current)
        return res