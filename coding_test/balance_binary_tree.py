from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            if abs(l - r) > 1:
                res[0] = False
                return 0 
            return max(l, r) + 1
        
        dfs(root)
        return res[0]

# Break out of recursive for optimization
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            if abs(l - r) > 1:
                raise ValueError
            return max(l, r) + 1
        try:
            dfs(root)
        except ValueError:
            return False
        return True