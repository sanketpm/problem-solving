from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root: TreeNode):
        res = []

        stk = deque()

        while True:
            while root:
                stk.append(root)
                root = root.left
            
            if not stk:
                break

            root = stk.pop()
            res.append(root.val)

            root = root.right

        return res; 

root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


root.right.left= TreeNode(5)
root.right.right = TreeNode(7)

print(Solution().inorder(root))