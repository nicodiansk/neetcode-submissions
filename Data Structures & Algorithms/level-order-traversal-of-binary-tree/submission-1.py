# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q=deque()
        q.append(root)
        res = []
        while q:
            current=[]
            lq=len(q)
            for i in range(lq):
                r = q.popleft()
                current.append(r.val)
                if r.left:
                    q.append(r.left) 
                if r.right:
                    q.append(r.right)
            res.append(current)
        return res
        
            