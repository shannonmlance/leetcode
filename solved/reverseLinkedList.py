# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->None
# Output: 5->4->3->2->1->None

# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# iterative solution is faster and uses less memory
class Solution:
    def reverseList(self, head):
        # if the head or the head.next are equal to None, return the head
        if not head or not head.next:
            return head
        # initiate a variable to store the recursive call
        # recursively call the method, passing in the next node
        temp = self.reverseList(head.next)
        # set the current head's next next to be the new head
        head.next.next = head
        # set the new head's next to none
        head.next = None
        # return the temp
        return temp

# same as below, just written in a more pythonic style
class pythonicIterativeSolution:
    def reverseList(self, head):
        cur, temp = head, None
        while cur:
            run, cur.next, temp, cur = cur.next, temp, cur, run
        return temp

class iterativeSolution:
    def reverseList(self, head):
        # initiate a variable to iterate through the list, and set its value as the head of the list
        current = head
        # initiate a variable for pointing backwards, and set its value equal to none
        temp = None
        # loop through the list as long as the current node exists
        while current != None:
            # initiate a variable to move ahead of the current node, so that the next node is not lost when the current node is reversed
            runner = current.next
            # point the current node backwards
            current.next = temp
            # increment the temp and current nodes
            temp = current
            current = runner
        # return the temp, as both the runner and the current variables will have moved outside of the list
        return temp

# implement a list
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

def printList(node):
    current = node
    while current != None:
        print(current.val)
        current = current.next
    return

s = Solution()
printList(None)
a = s.reverseList(None)
print("*"*10)
printList(a)
