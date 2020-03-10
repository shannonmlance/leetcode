# Given a binary search tree, find the lowest common ancestor of two given nodes in the BST. According to the definition of LCS on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)." The LCA is the shared ancestor of p and q that is located farthest from the root.

# Diagram of given binary search tree: root = [6,2,8,0,4,7,9,null,null,3,5]
#       6
#    /     \
#   2       8
#  / \     / \
# 0   4   7   9
#    / \
#   3   5

# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # base case
        # if the value of the root is equal to the value of either given nodes, then the root is the LCA
        if root.val == p.val or root.val == q.val:
            return root
        # if the first given node is greater than the second given node, reverse them so that they are sorted ascending
        if p.val > q.val:
            p, q = q, p
        # if the second given node is less than the root, recursively call this function passing in the root's left node as the new root
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if the first given node is greater than the root, recursively call this function passing in the root's right node as the new root
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

# implement a tree
one = TreeNode(6)
two = TreeNode(2)
three = TreeNode(8)
four = TreeNode(0)
five = TreeNode(4)
six = TreeNode(7)
seven = TreeNode(9)
eight = TreeNode(3)
nine = TreeNode(5)

one.left = two
one.right = three

two.left = four
two.right = five
three.left = six
three.right = seven

five.left = eight
five.right = nine

def printTree(node):
    if not node:
        return "Tree is empty"
    q = [node]
    while q:
        x = q.pop(0)
        if x == "null":
            print("null")
        else:
            print(x.val)
            if x.left:
                q.append(x.left)
            if not x.left:
                q.append("null")
            if x.right:
                q.append(x.right)
            if not x.right:
                q.append("null")

# printTree(one)
s = Solution()
a = s.lowestCommonAncestor(one, seven, four)
print("~"*10)
print(a.val)