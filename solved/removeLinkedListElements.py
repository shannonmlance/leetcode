# Remove all elements from a linked list of integers that have value val.

# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        # set the front runner at the head
        current = head
        # loop through as long as the front runner exists
        while current != None:
            # if the front runner's value is equal to the target value
            if current.val == val:
                # and if the front runner is at the head of the list
                if current == head:
                    # increment the head, thereby removing the original head
                    head = head.next
                    # reset the front runner at the new head
                    current = head
                # and if the front runner is not at the head of the list
                else:
                    # increment the front runner
                    current = current.next
                    # set the back runner to point to the incremented front runner, thereby removing the front runner
                    previous.next = current
            # if the front runner's value is not equal to the target value
            else:
                # increment both runners forward
                previous = current
                current = current.next
        return head

class mySolution:
    def removeElements(self, head, val):
        # loop as long as the head exists and the head's value is the target value
        while head != None and head.val == val:
            # move the head forward, thereby removing the original head
            head = head.next
        # if there is now no head, return
        if head == None:
            return head
        # set up two runners, one at the head and one at the head's next
        previous = head
        current = head.next
        # loop through until the front runner doesn't exist
        while current != None:
            # if the front runner's value is equal to the target value
            if current.val == val:
                # set the back runner to point to the front runner's next, thereby removing the front runner
                previous.next = current.next
                # reset the front runner to the next node
                current = current.next
            # if the front runner's value does not equal the target value
            else:
                # increment both runners forward
                previous = previous.next
                current = current.next
        return head

# stuff for making and checking the list
def printAll(node):
    print("*"*10)
    current = node
    while current != None:
        print(current.val)
        current = current.next
    print("*"*10)

one = ListNode(6)
two = ListNode(6)
three = ListNode(6)
four = ListNode(6)
five = ListNode(6)
six = ListNode(6)
seven = ListNode(6)
eight = ListNode(6)
nine = ListNode(6)
ten = ListNode(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten

s = Solution()
printAll(one)
a = s.removeElements(one, 6)
printAll(a)