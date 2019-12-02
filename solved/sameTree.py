# Given two binary trees, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]
# Output: true

# Example 2:
# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]
# Output: false

# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]
# Output: false

# [12,null,60][12,null,-72]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        # if both nodes do not exist, then the trees are the same
        if p == None and q == None:
            return True
        # if only one tree exists, then the trees are not the same
        if (p != None and q == None) or (p == None and q != None):
            return False
        # run recursive search to evaluate if the trees are the same
        a = self.depthFirst(p, q, True)
        return a
    # this method evaluates two nodes, each from the same place in two different trees, pass in a boolean to verify that the recursive search should continue
    def depthFirst(self, node1, node2, b):
        # if the values of both nodes are not the same, then the trees are not the same
        if node1.val != node2.val:
            return False
        # if the values of both nodes are the same, the the children of those nodes need to be evaluated
        else:
            # if the left children of both nodes exist, and the boolean proves that the tree is currently the same, recursively call this method to evaluate the left children
            if node1.left != None and node2.left != None and b == True:
                b = self.depthFirst(node1.left, node2.left, b)
            # if the right children of both nodes exist, and the boolean proves that the tree is currently the same, recursively call this method to evaluate the right children
            if node1.right != None and node2.right != None and b == True:
                b = self.depthFirst(node1.right, node2.right, b)
            # if the left or right child only exists for one node, then the trees are not the same
            if (node1.left != None and node2.left == None) or (node1.left == None and node2.left != None) or (node1.right != None and node2.right == None) or (node1.right == None and node2.right != None):
                return False
        return b

# build tree
firsta = TreeNode(12)
firstb = TreeNode(12)
# seconda = TreeNode(2)
# secondb = TreeNode(2)
thirda = TreeNode(60)
thirdb = TreeNode(-72)
# fourtha = TreeNode(4)
# fourthb = TreeNode(4)
# fiftha = TreeNode(5)
# fifthb = TreeNode(5)
# sixtha = TreeNode(6)
# sixthb = TreeNode(6)
# seventha = TreeNode(7)
# seventhb = TreeNode(7)
# eightha = TreeNode(8)
# eighthb = TreeNode(8)
# nintha = TreeNode(9)
# ninthb = TreeNode(9)
# tentha = TreeNode(10)
# tenthb = TreeNode(10)
# eleventha = TreeNode(11)
# eleventhb = TreeNode(11)
# twelftha = TreeNode(12)
# twelfthb = TreeNode(12)
# thirteentha = TreeNode(13)
# thirteenthb = TreeNode(13)
# fourteentha = TreeNode(14)
# fourteenthb = TreeNode(14)
# fifteentha = TreeNode(15)
# fifteenthb = TreeNode(15)

# firsta.left = seconda
# firstb.left = secondb
firsta.right = thirda
firstb.right = thirdb

# seconda.left = fourtha
# secondb.left = fourthb
# seconda.right = fiftha
# secondb.right = fifthb
# thirda.left = sixtha
# thirdb.left = sixthb
# thirda.right = seventha
# thirdb.right = seventhb

# # fourtha.left = eightha
# fourthb.left = eighthb
# # fourtha.right = nintha
# fourthb.right = ninthb
# # fiftha.left = tentha
# fifthb.left = tenthb
# # fiftha.right = eleventha
# fifthb.right = eleventhb
# # sixtha.left = twelftha
# sixthb.left = twelfthb
# # sixtha.right = thirteentha
# sixthb.right = thirteenthb
# # seventha.left = fourteentha
# seventhb.left = fourteenthb
# # seventha.right = fifteentha
# seventhb.right = fifteenthb

def printTree(node):
    print(node.val)
    if node.left != None:
        printTree(node.left)
    if node.right != None:
        printTree(node.right)

printTree(firsta)
print("*"*20)
printTree(firstb)
print("*"*20)

s = Solution()
a = s.isSameTree(firsta, firstb)
print(a)