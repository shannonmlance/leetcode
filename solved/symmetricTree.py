# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
 
# Note:
# Bonus points if you could solve it both recursively and iteratively.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        # if there is no root, then the tree is symmetrical by default
        if root == None:
            return True
        # if there are no branches, then the tree is symmetrical
        if root.left == None and root.right == None:
            return True
        # if there is only one branch, then the tree cannot be symmetrical
        if (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        # initiate queues for both sides of the tree
        qleft = []
        qright = []
        # add the left and right branch to their corresponding queues
        qleft.append(root.left)
        qright.append(root.right)
        # continue moving through the tree as long as there are nodes in both queues
        while len(qleft) > 0 and len(qright) > 0:
            # remove the first node from each queue
            left = qleft.pop(0)
            right = qright.pop(0)
            # if both nodes have the same value
            if left.val == right.val:
                # if both nodes have mirror-image children, add those children to their corresponding queues
                if left.left != None and right.right != None:
                    qleft.append(left.left)
                    qright.append(right.right)
                if left.right != None and right.left != None:
                    qleft.append(left.right)
                    qright.append(right.left)
                # if the children nodes are not in mirror-image placement, then the tree cannot be symmetrical
                if (left.left != None and right.right == None) or (left.left == None and right.right != None) or (left.right != None and right.left == None) or (left.right == None and right.left != None):
                    return False
            # if the two nodes do not have the same value, then the tree is not symmetrical
            else:
                return False
        # once the end of the tree is reached, if it has not been deemed unsymmetrical yet, then by default it is symmetrical
        return True

# build tree

first = TreeNode(1)
second = TreeNode(2)
two = TreeNode(2)
third = TreeNode(3)
three = TreeNode(3)
fourth = TreeNode(4)
four = TreeNode(4)
fifth = TreeNode(5)
five = TreeNode(5)
sixth = TreeNode(6)
six = TreeNode(6)
seventh = TreeNode(7)
seven = TreeNode(7)
eighth = TreeNode(8)
eight = TreeNode(8)
ninth = TreeNode(9)
nine = TreeNode(9)

# [2,3,3,4,5,5,4,6,null,8,9,9,8,null,6]

# first.left = second
# first.right = two

second.left = third
second.right = three
# two.left = four
# two.right = three

third.left = fourth
third.right = fifth
three.left = five
three.right = four
fourth.left = sixth
# fourth.right = seventh
# four.left = seven
four.right = six
fifth.left = eighth
fifth.right = ninth
five.left = nine
five.right = eight

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

printLevel(second)
print("*"*20)

s = Solution()
a = s.isSymmetric(second)
print("The tree is symmetrical:", a)