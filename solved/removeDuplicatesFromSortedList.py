# Given a sorted linked list, delete all duplicates such that each element appears only once.

# Example 1:
# Input: 1->1->2
# Output: 1->2

# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        # if the list is empty or contains only one node, then there can be no duplicates so return the list as is
        if head == None or head.next == None:
            return head
        else:
            # create a runner variable to move over the list and set it at the beginning of the list
            current = head
            # move through the list until reaching the last node
            while current.next != None:
                # if the current node and the next one have the same value
                if current.val == current.next.val:
                    # set the current node to point to the one after the next, thereby removing the duplicate from the list
                    current.next = current.next.next
                # if the current node and the next one do not have the same value
                else:
                    # move the runner to the next node
                    current = current.next
        # return the beginning of the list
        return head

first = ListNode(3)
second = ListNode(3)
third = ListNode(3)
fourth = ListNode(3)
fifth = ListNode(3)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("LIST")
temp = first
while temp != None:
    print(temp.val)
    temp = temp.next
print("*"*20)
s = Solution()
a = s.deleteDuplicates(first)
print(a)
