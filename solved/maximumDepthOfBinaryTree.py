# Given a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # base case
        # if there is no root, there is no depth
        if root == None:
            return 0
        else:
            # recursively call the method on the left side of the root
            lheight = self.maxDepth(root.left)
            # recursively call the method on the right side of the root
            rheight = self.maxDepth(root.right)
            # if the left side has a greater height than the right side, return that height, plus one to account for the current level
            if lheight > rheight:
                return lheight + 1
            # if the left side does not have a greater height than the right side, return the right side's height, plus one to account for the current level
            else:
                return rheight + 1

# build tree

first = TreeNode(1)
second = TreeNode(2)
third = TreeNode(3)
fourth = TreeNode(4)
fifth = TreeNode(5)
sixth = TreeNode(6)
seventh = TreeNode(7)
eighth = TreeNode(8)
ninth = TreeNode(9)
tenth = TreeNode(10)

first.left = second
first.right = third
second.left = fourth
third.left = fifth
third.right = sixth
sixth.left = seventh
sixth.right = eighth
seventh.left = ninth
ninth.right = tenth

def printLevel(node):
    h = height(node)
    for i in range(1, h+1):
        print("*"*20)
        givenLevel(node, i)

def height(node):
    if node == None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def givenLevel(node, level):
    if node == None:
        print("tree is empty")
        return
    if level == 1:
        print(node.val)
    if level > 1:
        givenLevel(node.left, level-1)
        givenLevel(node.right, level-1)

printLevel(first)
print("*"*20)

s = Solution()
a = s.maxDepth(first)
print(a)
