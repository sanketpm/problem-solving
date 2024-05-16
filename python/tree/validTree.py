# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBst(self, root: TreeNode, min: int, max: int):
        if not root:
            return True

        if root.val > min and root.val < max:
            return ( 
                    self.isValidBst(root.left, min, root.val) and 
                    self.isValidBst(root.right, root.val, max)
                    )
        
        return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBst(root, -float('inf'), float('inf'))

