# Given an array where elements are sorted in ascending order, convert it to a height balanced BST. For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Solution:
    def sortedArrayToBST(self, nums):
        # if the array is empty, there can be no tree
        if len(nums) == 0:
            return None
        # if the array contains only one number, that is the root
        if len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        # if the array contains two numbers, make the first one the root and the second one the right child, as the array is sorted
        if len(nums) == 2:
            root = TreeNode(nums[0])
            root.right = TreeNode(nums[1])
            return root
        # find the middle of the array
        mid = math.floor((len(nums) - 1) / 2)
        # make the middle of the array the root of the tree
        root = TreeNode(nums[mid])
        # use a recursive method to add the left side of the array to the left side of the tree
        self.addNode(nums, root, 0, mid)
        # use a recursive method to add the right side of the array to the right side of the tree
        self.addNode(nums, root, mid + 1, len(nums))
        return root
    # method for recursively adding nodes from an array to a tree
    def addNode(self, nums, root, start, end):
        # base case
        # if the beginning and end of the given portion of the array are the same value, there is nothing more to add
        if start == end:
            return
        # find the middle of the given portion of the array
        mid = math.floor((end - start) / 2) + start
        # make the middle of the given portion of the array the node to be added to the tree
        node = TreeNode(nums[mid])
        # if the value of the parent node is greater than the value of the child node, add the child node to the left side of the parent node
        if root.val > node.val:
            root.left = node
        # if the value of the parent node is not greater than the value of the child node, add the child node to the right side of the parent node
        else:
            root.right = node
        # recursively continue adding the array to the tree
        self.addNode(nums, node, start, mid)
        self.addNode(nums, node, mid + 1, end)
        return
    def printTreeDFS(self, root):
        if root != None:
            print(root.val)
            self.printTreeDFS(root.left)
            self.printTreeDFS(root.right)
        else:
            print("no leaf here")
        return
    def printTreeBFS(self,root):
        if root == None:
            print("tree is empty")
            return
        q = []
        q.append(root)
        while len(q) > 0:
            node = q.pop(0)
            if node == None:
                print("null")
            else:
                print(node.val)
                q.append(node.left)
                q.append(node.right)
        return

# find the mid point of the array
# set that as the root
# find the mid point between the root and the beginning of the array
    # set that as the root.left
# find the mid point between the root and the end of the array
    # set that as the root.right
# repeat using the root.left as the root and the root of root.left as the end of the array
# repeat using the root.right as the root and the root of root.right as the beginning of the array

s = Solution()
a = s.sortedArrayToBST(nums)
print("~"*20)
s.printTreeDFS(a)
print("~"*20)
# s.printTreeBFS(a)


    #                         0
    #                     /       \
    #                 -5              5
    #             /       \          /       \
    #         -8        -2          3         8
    #     /     \      /  \       /  \       /   \
    #     -9    -7    -3  -1     2   4      7     9
    #   /  \   / \     /\ /\     /\  /\    /\     /\
    # -10        -6   -4        1         6        10