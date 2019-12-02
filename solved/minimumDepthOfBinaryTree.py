# Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

#     3
#    / \
#      20

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        # call a method that does a depth first search for the first node from the root which has no children
        count = self.DFS(root, 1)
        return count
    # method for finding the first node from the given node which has no children, using depth first recursive search
    def DFS(self, node, count):
        # if the given node does not exist, then there is no depth
        if node == None:
            return count - 1
        # if there are no children for the given node, then it is as deep as it can go
        if node.left == None and node.right == None:
            return count
        else:
            # initilize a left and right side counter
            lcount = None
            rcount = None
            # if the given node has a left side, recursively find the depth of the children of the left side
            if node.left != None:
                lcount = self.DFS(node.left, count + 1)
            # if the given node has a right side, recursively find the depth of the children of the right side
            if node.right != None:
                rcount = self.DFS(node.right, count + 1)
            # if the given node did not have a left side, return the depth of the right side
            if lcount == None:
                return rcount
            # if the given node did not have a right side, return the depth of the left side
            if rcount == None:
                return lcount
            # if the given node had both sides, return the side with the shortest depth
            if rcount <= lcount:
                return rcount
            if lcount < rcount:
                return lcount

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
eleventh = TreeNode(11)
twelfth = TreeNode(12)
thirteenth = TreeNode(13)
fourteenth = TreeNode(14)
fifteenth = TreeNode(15)

first.left = second
first.right = third

second.left = fourth
second.right = fifth
third.left = sixth
third.right = seventh

fourth.left = eighth
fourth.right = ninth
fifth.left = tenth
fifth.right = eleventh
sixth.left = twelfth
sixth.right = thirteenth
seventh.left = fourteenth
seventh.right = fifteenth

def countLevels(root):
    h = height(root)
    for i in range(1, h + 1):
        print("*"*10)
        printLevel(root, i)
    return

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

def printLevel(node, level):
    if node == None:
        print("null")
        return
    if level == 1:
        print(node.val)
    else:
        printLevel(node.left, level - 1)
        printLevel(node.right, level - 1)
    return

countLevels(first)
print("~"*20)

s = Solution()
a = s.minDepth(first)
print(a)
