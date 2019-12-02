# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        # find the height of the tree
        h = self.height(root)
        # initiate an empty array to store the levels of the tree
        arr = []
        # initiate a level counter
        j = 0
        # loop through each level of the tree, starting at the bottom
        for i in range(h, 0, -1):
            # add to the array that is storing the levels of the tree an empty array to store the values at the current level
            arr.append([])
            # this method will add all the values at the given level to the array
            self.printLevel(root, i, arr[j])
            # increment the level counter
            j += 1
        # return the entire array, containing arrays of all the values of each level, from the bottom of the tree to the top of the tree
        return arr
    # method for finding and returning the height of a tree
    def height(self, root):
        # if the root does not exist, then the height is 0
        if root == None:
            return 0
        # if the root exists
        else:
            # recursively call the method on the left side of the tree
            lheight = self.height(root.left)
            # recursively call the method on the right side of the tree
            rheight = self.height(root.right)
            # if the left side is taller than the right side, return the height of the left side plus one, to account for the current level
            if lheight > rheight:
                return lheight + 1
            # if the left side is not taller than the right side, return the height of the right side plus one, to account for the current level
            else:
                return rheight + 1
    # method for adding all the values of a given level of a tree, left to right, to an array
    def printLevel(self, node, level, arr):
        # if the node does not exist, do not add it to the array
        if node == None:
            return
        # if the given level is the current level to be added, add the value of the node to the array
        elif level == 1:
            arr.append(node.val)
        # if the given level is more than the current level to be added, then recursively call the method on the right and left sides of the node
        else:
            self.printLevel(node.left, level - 1, arr)
            self.printLevel(node.right, level - 1, arr)

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
        return
    if level == 1:
        print(node.val)
    if level > 1:
        givenLevel(node.left, level-1)
        givenLevel(node.right, level-1)

printLevel(first)
print("*"*20)

s = Solution()
a = s.levelOrderBottom(first)
print(a)