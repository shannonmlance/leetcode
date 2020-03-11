# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:
# Input:
    #    1
    #  /   \
    # 2     3
    #  \
    #   5
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        # initiate an array to hold the final list of paths
        l = []
        # if there is a given root
        if root:
            # initiate a string with the value of the root
            s = str(root.val)
            # call the helper method to find all the paths from the root
            self.subPaths(l, s, root)
        # return the list of paths
        return l
    # helper method to find all the paths from the root
    def subPaths(self, l, s, node):
        # if the given node has a left node
        if node.left:
            # initiate a left string variable to maintain the integrity of the original given string
            sl = s
            # add to the left string variable the "next" marker and the value of the left node
            sl += "->" + str(node.left.val)
            # if the left node has a left or right node
            if node.left.left or node.left.right:
                # recursively call this method, passing in the updated string and the left node
                self.subPaths(l, sl, node.left)
            # if the left node has neither a left or right node
            else:
                # add the left string to the list of paths
                l.append(sl)
        # if the given node has a right node
        if node.right:
            # initiate a right string variable to maintain the integrity of the original given string
            sr = s
            # add to the right string variable the "next" marker adn the value of the right node
            sr += "->" + str(node.right.val)
            # if the right node has a left or right node
            if node.right.left or node.right.right:
                # recursively call this method, passing in the updated string and the right node
                self.subPaths(l, sr, node.right)
            # if the right node has neither a left or right node
            else:
                # add the right string to the list of paths
                l.append(sr)
        # if the given node has neither a left or right node
        if not node.left and not node.right:
            # add the given string to the list of paths
            l.append(s)
        # does not need to return anything, due to memoization
        return

# create tree
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c

b.left = d
b.right = e
c.left = f
c.right = g

def printTreeDFS(node):
    if node:
        print(node.val)
        printTreeDFS(node.left)
        printTreeDFS(node.right)

def printTreeBFS(node):
    q = [node]
    while q:
        x = q.pop(0)
        print(x.val)
        if x.left:
            q.append(x.left)
        if x.right:
            q.append(x.right)

printTreeDFS(a)
print("~"*10)
printTreeBFS(a)
print("~"*10)
sol = Solution()
ans = sol.binaryTreePaths(a)
print(ans)