# Given a linked list, determine if it has a cycle in it. To represent a cycle in the given linked list, we use an integer 'pos' which represents the position (0-indexed) in the linked list where tail connects to. If 'pos' is -1, then there is no cycle in the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# more clearly written:
class Solution:
    def hasCycle(self, head):
        if head == None:
            print("one or less")
            return False
        current = head
        runner = head.next
        while current != runner:
            if runner == None or runner.next == None:
                return False
            current = current.next
            runner = runner.next.next
        return True

class mySolution:
    def hasCycle(self, head):
        # if the list is empty, or has only one node that doesn't loop to itself, then there is no loop
        if head == None or head.next == None:
            return False
        # initiate a slow runner and a fast runner
        current = head
        runner = head.next
        # while the fast runner exists
        while runner != None:
            # if the slow runner and the fast runner are on the same node, then there must be a loop
            if current == runner:
                return True
            # if the fast runner's next node does not exist, then the end of the list has been reached and there is no loop
            if runner.next == None:
                return False
            # if the fast runner's next next node does not exist, then the end of the list has been reached and there is no loop
            if runner.next.next == None:
                return False
            # iterate the slow runner by one node
            current = current.next
            # iterate the fast runner by two nodes
            runner = runner.next.next
        # if the runner no longer exists, then the end of the list has been reached and there is no loop
        return False

# create list
class List:
    def __init__(self):
        self.head = None
    def addNode(self, x):
        node = ListNode(x)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        return
    def printList(self, node):
        print("*"*20)
        current = node
        while current != None:
            print(current.val)
            current = current.next
        print("*"*20)
        return
    def createListFromArray(self, arr):
        for i in range(len(arr)):
            self.addNode(arr[i])
        return
    def createLoop(self, pos):
        if pos < 0:
            print("No loop")
        elif self.head == None:
            print("List is empty")
        else:
            count = 0
            current = self.head
            while current.next != None:
                if count == pos:
                    loop = current
                current = current.next
                count += 1
            if count < pos:
                print("loop is out of range")
            elif count == pos:
                current.next = current
            else:
                current.next = loop
        return

arr = [3,5,6,7,1,9,2,8]
l = List()
l.createListFromArray(arr)
# l.printList(l.head)
l.createLoop(-1)
# l.printList(l.head)

s = Solution()
a = s.hasCycle(l.head)
print(a)