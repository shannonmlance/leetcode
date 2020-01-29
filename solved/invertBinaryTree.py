# Invert a binary tree.

# Example:
# Input:
#          4
#        /   \
#       2     7
#      / \   / \
#     1   3 6   9
# Output:
#          4
#        /   \
#       7     2
#      / \   / \
#     9   6 3   1

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        # if the root doesn't exist, just return
        if not root:
            return
        # if there is a node to the root's left, recursively call the function, passing in the left node
        if root.left:
            self.invertTree(root.left)
        # if there is a node to the root's right, recursively call the function, passing in the right node
        if root.right:
            self.invertTree(root.right)
        # swap the left node with the right node
        temp = root.left
        root.left = root.right
        root.right = temp
        return root

# initiate tree
a = TreeNode(1)

b = TreeNode(2)
c = TreeNode(3)

d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

h = TreeNode(8)
i = TreeNode(9)
j = TreeNode(10)
k = TreeNode(11)
l = TreeNode(12)
m = TreeNode(13)
n = TreeNode(14)
o = TreeNode(15)

a.left = b
# a.right = c

b.left = d
# b.right = e
c.left = f
c.right = g

d.left = h
# d.right = i
e.left = j
e.right = k

f.left = l
f.right = m
g.left = n
g.right = o

# method for checking tree construction
def printBF(node):
    if not node:
        return
    q = []
    q.append(node)
    while len(q) > 0:
        print(q[0].val)
        n = q.pop(0)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return

# method for printing each level of the tree
def printLO(node):
    h = height(node)
    for i in range(1, h+1):
        print("~"*10)
        printGL(node, i)
def printGL(node, level):
    if not node:
        print("None")
    elif level == 1:
        print(node.val)
    else:
        printGL(node.left, level - 1)
        printGL(node.right, level - 1)
def height(node):
    if not node:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)
    return max(lheight,rheight) + 1

printBF(a)
printLO(a)
print("*"*10)
s = Solution()
ans = s.invertTree(a)
printBF(ans)
printLO(ans)