# Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as: a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        # if root is empty, there is no tree and by default it is balanced
        if root == None:
            return True
        # check the maximum height of the left and right subtrees
        left = self.height(root.left)
        right = self.height(root.right)
        # if the height difference between the two subtrees is greater than 1, then the tree is not balanced
        if abs(left - right) > 1:
            return False
        # if the height difference between the two subtrees is not greater than 1, there is a possibility that the tree is balanced
        else:
            # set a default boolean of true
            b = True
            # if left has height, then the subtrees of left need to be checked
            if left > 0:
                # b can be changed to false if the subtrees of the left side are not balanced
                b = self.isBalanced(root.left)
            # if the right has height, then the subtrees of right need to be checked, but only if the left side was balanced
            if right > 0 and b == True:
                # again, b can be changed to false if the subtrees of the right side are not balanced
                b = self.isBalanced(root.right)
            # if left and right have no subtrees, then the tree is balanced and the default boolean will be returned
            # if left and right had subtrees, then the value that was returned from the recursive check will be returned
            return b
    # method for returning the maximum height of a given node
    def height(self, node):
        # base case
        # if the node does not exist, then there is no height
        if node == None:
            return 0
        # if the node does exist, need to calculate the height of both the left and right side
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            # if the height of the left side is more than the height of the right side, return the height of the left side, plus one to account for the current level
            if lheight > rheight:
                return lheight + 1
            # if the height of the left side is not more than the height of the right side, return the height of the right side, plus one to account for the current level
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
eleventh = TreeNode(11)
twelfth = TreeNode(12)
thirteenth = TreeNode(13)
fourteenth = TreeNode(14)
fifteenth = TreeNode(15)

first.left = second
first.right = third
second.left = fourth
second.right = fifth
# third.left = sixth
third.right = seventh
fourth.left = eighth
fourth.right = ninth
fifth.left = tenth
fifth.right = eleventh
sixth.left = twelfth
sixth.right = thirteenth
seventh.left = fourteenth
seventh.right = fifteenth

# print tree depth first
def printDFS(node):
    if node == None:
        print("null")
    else:
        print(node.val)
        printDFS(node.left)
        printDFS(node.right)
    return

def printBFS(node):
    if node == None:
        print("null")
    else:
        q = []
        q.append(node)
        while len(q) > 0:
            n = q.pop(0)
            print(n.val)
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right)
    return

def printLevels(node):
    if node == None:
        print("null")
        return
    h = height(node)
    for i in range(0, h):
        print("*"*5, "level", i, "*"*5)
        printLevel(node, i)
    return

def height(node):
    if node == None:
        return 0
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
    if level == 0:
        print(node.val)
    else:
        printLevel(node.left, level - 1)
        printLevel(node.right, level - 1)
    return

# printDFS(first)
# print("~"*20)
# printBFS(first)
# print("~"*20)
printLevels(first)

print("~"*20)

s = Solution()
a = s.isBalanced(first)
print(a)