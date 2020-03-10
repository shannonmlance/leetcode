# Write a function to delete a node (except the tail) in a singly-linked list, given only access to that node.

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

# Note:
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        # copy the value from the next node into the current node (essentially making the current node equal to the next node)
        node.val = node.next.val
        # change the current node's pointer to skip the next node and point at the one after that (essentially "deleting" the next node, which is okay because the current node is now the "next node")
        node.next = node.next.next