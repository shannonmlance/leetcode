# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

sum = 22

class Solution:
    def hasPathSum(self, root, sum):
        # if the root doesn't exist, there can be no path
        if root == None:
            return False
        # if the value of the root is equal to the sum, and the root is a leaf (has no children), the path is finished and the sum has been found
        if root.val == sum and root.left == None and root.right == None:
            return True
        # if neither of the above base cases have been met, need to continue traversing the tree
        else:
            # recursively call the method, passing in the left side of the root, and reducing the sum by the value of the root
            b = self.hasPathSum(root.left, sum - root.val)
            # if the left side returned a false
            if b == False:
                # recursively call the method, passing in the right side of the root, and reducing the sum by the value of the root
                b = self.hasPathSum(root.right, sum - root.val)
            # return the boolean from the left side if it was True, otherwise return the boolean from the right side
            return b

# build tree
one = TreeNode(5)
two = TreeNode(4)
three = TreeNode(8)
four = TreeNode(11)
# five = TreeNode(5)
six = TreeNode(13)
seven = TreeNode(4)
eight = TreeNode(7)
nine = TreeNode(2)
# ten = TreeNode(10)
# eleven = TreeNode(11)
# twelve = TreeNode(12)
# thirteen = TreeNode(13)
fourteen = TreeNode(1)
# fifteen = TreeNode(15)

one.left = two
one.right = three
two.left = four
# two.right = five
three.left = six
three.right = seven
four.left = eight
four.right = nine
# five.left = ten
# five.right = eleven
# six.left = twelve
# six.right = thirteen
seven.left = fourteen
# seven.right = fifteen

def printTree(root):
    h = height(root)
    for i in range(1, h+1):
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

printTree(one)
print("~"*20)

s = Solution()
a = s.hasPathSum(one, sum)
print(a)