from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if root == None:
            return ""
        
        q = deque()
        res = ""

        q.append(root)

        while q:
            node = q.popleft()

            if node == None:
                res += '#,'
            else:
                res += str(node.val) +','

                q.append(node.left)           
                q.append(node.right)           
        
        return res
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

# print(Codec().serialize(root))

s = '1,2,3,#,#,4,5,#,#,#,#,'

nodes = s.split(',')
print(nodes)

lvl = 0
root = TreeNode(nodes[0])

q = deque()
q.append(root)

for i in range(1, len(nodes)):
    parent = q.popleft()

    if nodes[i] != '#':
        root.left = TreeNode(int(nodes[i]))
        q.append(root.left)

    if nodes[i + 1] != '#':
        root.right = TreeNode(int(nodes[i + 1]))
        q.append(root.right)

print(root)
