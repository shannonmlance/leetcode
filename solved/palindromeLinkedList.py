# Given a singly linked list, determine if it is a palindrome.

# Example 1:
# Input: 1->2
# Output: false

# Example 2:
# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# this solution is super cool and requires less markers and while loops
class Solution:
    def isPalindrome(self, head):
        # initiate a reverse marker with a value of none
        rev = None
        # set two runners at the head
        slow = fast = head
        # as long as the fast runner exists and has one node in front of it
        while fast and fast.next:
            # increment the fast runner by two nodes
            # set the reverse marker equal to the slow marker
            # set the reverse marker to point to the place where the reverse marker used to be
            # increment the slow marker by one node
            fast, rev, rev.next, slow = fast.next.next, slow, rev, slow.next
        # if the fast runner exists (happens when the list contains an even number of nodes)
        if fast:
            # increment the slow runner by one node
            slow = slow.next
        # as long as the reverse marker exists and as long as the reverse marker's value is equal to the slow marker's value
        while rev and rev.val == slow.val:
            # increment the reverse marker and the slow marker by one node
            rev, slow = rev.next, slow.next
        # return False if the reverse marker exists and True if the reverse marker is equal to none
        # this is because if the reverse marker exists, it exited the above while loop due to the values not matching. If the reverse marker is equal to none, it made it all the way through the list, with all values matching
        return not rev

# my solution works great, takes O(n) time and O(1) space
class mySolution:
    def isPalindrome(self, head):
        # if there are less than two nodes in the list, then it is a palindrome by default
        if not head or not head.next:
            return True
        # if there are only two nodes in the list
        if not head.next.next:
            # and if those two nodes have the same value, then it is a palindrome
            if head.val == head.next.val:
                return True
            # and if those two nodes do not have the same value, then it is not a palindrome
            return False
        # set two runners at the head
        slow = fast = head
        # while the fast runner has two nodes in front of it
        while fast.next and fast.next.next:
            # increment the slow runner by one node and the fast runner by two nodes
            slow, fast = slow.next, fast.next.next
        # if there's still one node in front of the fast runner (happens when lists contain an even number of nodes)
        if fast.next:
            # set a previous marker at the slow runner's place and increment the slow and fast runner by one node
            prev, slow, fast = slow, slow.next, fast.next
            # set the previous marker to point to none
            prev.next = None
        # set (or move) the previous marker to the slow runner's place
        # set a current marker to the node in front of the slow runner's place
        # increment the slow runner by two nodes
        prev, curr, slow = slow, slow.next, slow.next.next
        # set the previous marker to point to none
        prev.next = None
        # as long as the slow marker exists
        while slow:
            # set the current marker to point to the previous marker
            curr.next = prev
            # move the previous marker to the current marker's place
            # move the current marker to the slow marker's place
            # increment the slow marker by one node
            prev, curr, slow = curr, slow, slow.next
        # set the current marker to point to the previous marker
        curr.next = prev
        # as long as the current marker exists
        while curr:
            # if the head marker's value is not equal to the current marker's value, the it is not a palindrome
            if head.val != curr.val:
                return False
            # increment the head marker and the current marker by one node
            head = head.next
            curr = curr.next
        # upon reaching the end of the list, from both directions, the list must be a palindrome
        return True


# generate linked list
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(5)
seven = ListNode(4)
eight = ListNode(3)
nine = ListNode(2)
ten = ListNode(1)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten

def printList(node):
    current = node
    while current != None:
        print(current.val)
        current = current.next

printList(one)
s = Solution()
a = s.isPalindrome(one)
print(a)