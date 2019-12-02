# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # if list 1 is empty, we only need to return list two, as it is already sorted
        if l1 == None:
            return l2
        # if list 2 is empty, we only need to return list one, as it is already sorted
        if l2 == None:
            return l1
        # if the first node in list one has a smaller value than the first node in list two
        if l1.val < l2.val:
            # put the first node of list one into the merged list
            merged = l1
            # increment the marker of list one
            l1 = l1.next
        # if the first node in list one has an equal or larger value than the first node in list one
        else:
            # put the first node of list two into the merged list
            merged = l2
            # increment the marker of list two
            l2 = l2.next
        # set an iterator for the merged list at the beginning of the merged list
        runner = merged
        # as long as the markers of list one and list two have a value other than none
        while l1 != None and l2 != None:
            # if the node at the marker for list one has a smaller value than the node at the marker for list two
            if l1.val <= l2.val:
                # put the node at the marker of list one at the end of the merged list
                runner.next = l1
                # increment the marker of list one
                l1 = l1.next
            # if the node at the marker for list one has an equal or larger value than the node at the marker for list two
            else:
                # put the node at the marker of list two at the end of the merged list
                runner.next = l2
                # increment the marker of list two
                l2 = l2.next
            # increment the iterator for the merged list
            runner = runner.next
        # once one of the markers of list one and list two has a value of none, check if either list has any more nodes
        # if list one has more nodes that haven't been added to the merged list
        if l1 != None:
            # put the remaining list at the end of the merged list
            runner.next = l1
        # if list two has more nodes that haven't been added to the merged list
        if l2 != None:
            # put the remaining list at the end of the merged list
            runner.next = l2
        # once all nodes have been added, in order, return the first node of the merged list
        return merged

first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
sixth = ListNode(6)
seventh = ListNode(7)
eighth = ListNode(8)

list1 = fifth
fifth.next = sixth
sixth.next = seventh
seventh.next = eighth

print("printing first list")
temp = list1
while temp != None:
    print(temp.val)
    temp = temp.next

list2 = first
first.next = second
second.next = third
third.next = fourth

print("printing second list")
temp = list2
while temp != None:
    print(temp.val)
    temp = temp.next

s = Solution()
a = s.mergeTwoLists(list1, list2)

print("printing sorted merged list")
temp = a
while temp != None:
    print(temp.val)
    temp = temp.next

