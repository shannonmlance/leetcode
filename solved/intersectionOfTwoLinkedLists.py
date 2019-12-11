# Write a program to find the node at which the intersection of two singly linked lists begins.

# Example 1:
# A:      4 -> 1 -\
#                   8 -> 4 -> 5
# B: 5 -> 0 -> 1 -/
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head o fA, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; there are 3 modes before the intersected node in B.

# Example 2:
# A: 0 -> 9 -> 1 -\
#                   2 -> 4
# B:           3 -/
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; there is 1 node before the intersected node in B.

# Example 3:
# A: 2 -> 6 -> 4

# B:      1 -> 5
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.

# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# create lists
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    def printList(self, head):
        print("*"*20)
        print("Here's the list:")
        current = self.head
        while current != None:
            print(current, current.val)
            current = current.next
        return
    def listFromArray(self, arr):
        for i in range(len(arr)):
            self.addNode(arr[i])
        return

def mergeLists(headA, headB, skipA):
    if headA == None or headB == None:
        return
    currentA = headA
    count = 0
    while currentA != None:
        if count == skipA:
            break
        currentA = currentA.next
        count += 1
    currentB = headB
    while currentB.next != None:
        currentB = currentB.next
    currentB.next = currentA
    return

class mySolution:
    def getIntersectionNode(self, headA, headB):
        # initiate two pointers, one for each list
        currentA = headA
        currentB = headB
        # loop until both pointers equal none
        while currentA != None and currentB != None:
            # if the two pointers are pointing to the same node, then the intersected node has been found so return it
            if currentA == currentB:
                return currentA
            # if the two pointers are not pointing to the same node, and the two pointers are each at the end of their respective list, then there is no intersected node
            elif currentA.next == None and currentB.next == None:
                return None
            # if the two pointers are not pointing to the same node, and one pointer is at the end of its list, move it to the beginning of the other list and increment the other pointer
            elif currentA.next == None:
                currentA = headB
                currentB = currentB.next
            elif currentB.next == None:
                currentA = currentA.next
                currentB = headA
            # if none of the above exceptions are true, increment both pointers
            else:
                currentA = currentA.next
                currentB = currentB.next
        return

# establish two lists merged
arrayA = [1,3,5,7,9,11,13,15,17,19,21]
arrayB = [2]
listA = List()
listA.listFromArray(arrayA)
print("\nPrinting ListA")
listA.printList(listA.head)
listB = List()
listB.listFromArray(arrayB)
print("\nPrinting ListB")
listB.printList(listB.head)
mergeLists(listA.head, listB.head, 11)
print("\nPrinting ListA")
listA.printList(listA.head)
print("\nPrinting ListB")
listB.printList(listB.head)

# run solution
s = Solution()
a = s.getIntersectionNode(listA.head, listB.head)
print("\nANSWER")
print("-"*20)
print(a)