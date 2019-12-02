// scoping to function, to avoid window errors while testing
function NodeStuff() {
    // define singly-linked node
    class SLNode {
        constructor(val) {
            this.val = val;
            this.next = null;
        }
    }
    
    // define linked list
    class LinkedList {
        constructor() {
            this.head = null;
        }
        // provide a function for adding nodes to the linked list
        add(val) {
            // create a new singly-linked node, with the given value, and point to it with a variable
            var newNode = new SLNode(val);
            // if the list is empty
            if (this.head == null) {
                // point the head to the new node
                this.head = newNode;
            }
            // otherwise
            else {
                // create a current node marker and set at the beginning of the list
                var current = this.head;
                // iterate through the list
                while (current.next != null) {
                    current = current.next;
                }
                // add the new node to the end of the list
                current.next = newNode;
            }
            return this;
        }
        // provide a function for removing nodes from the linked list, based on given value
        remove(val) {
            // if the list is empty
            if (this.head == null) {
                // return the empty list
                return this;
            }
            // otherwise, if the head node is the same as the given value
            else if (this.head.val == val) {
                // move the head pointer to the second node, thereby removing the head node from the list
                this.head = this.head.next;
                // return the modified list
                return this;
            }
            // otherwise
            else {
                // create a current node marker and set at the beginning of the list
                var current = this.head;
                // iterate through the list
                while (current.next != null) {
                    // if the current node's next node's value is equal to the given value
                    if (current.next.val == val) {
                        // move the current node's next pointer to the following node, thereby removing the current node's next node
                        current.next = current.next.next;
                        // return the modified list
                        return this;
                    }
                    // otherwise
                    else {
                        // increment
                        current = current.next;
                    }
                }
                // a node with the given value was never found, return the unmodified list
                return this;
            }
        }
        // provide a function for finding duplicate values and removing all nodes that contain that duplicate value
        removeDuplicates(){
            // if the list is empty, there can be no duplicates
            if (this.head == null) {
                // return the unmodified list
                return this;
            }
            // otherwise, if the list contains only one node, there can be no duplicates
            else if (this.head.next == null) {
                // return the unmodified list
                return this;
            }
            // otherwise
            else {
                // create a current node marker and set at the beginning of the list
                var current = this.head;
                // create a previous node marker and set at the beginning of the list
                var previous = this.head;
                // iterate through the list
                while (previous.next != null) {
                    // set a found duplicates flag and set it to false
                    var foundDup = false;
                    // create a runner node marker for iterating through the list
                    var runner = current;
                    // iterate through the list
                    while (runner.next != null) {
                        // if the values are the same
                        if (current.val == runner.next.val) {
                            // set the found duplicates flag to true
                            foundDup = true;
                            // remove the runner node
                            runner.next = runner.next.next;
                        }
                        // otherwise
                        else {
                            // increment
                            runner = runner.next;
                        }
                    }
                    // once finished with the iteration, if the found duplicates flag is true
                    if (foundDup == true) {
                        // remove the node at the current node marker
                        // if the current node marker is at the head node
                        if (current == this.head) {
                            // remove the head node
                            this.head = this.head.next;
                        }
                        // otherwise
                        else {
                            // remove the current node
                            previous.next = previous.next.next;
                            // set current node for the next iteration
                            current = previous.next;
                        }
                    }
                    // otherwise
                    else {
                        // if the current node marker is at the head node
                        if (current == this.head) {
                            // increment the current node
                            current = current.next;
                        }
                        // otherwise
                        else {
                            // increment the current node and the previous node
                            current = current.next;
                            previous = previous.next;
                        }
                    }
                }
                // return the list
                return this;
            }
        }
    }
    // create a new linked list, and store it in a variable
    var list = new LinkedList();
    // create nodes and add them to the list
    list.add(1).add(2).add(8).add(0).add(9).add(3).add(5).add(9).add(9).add(7).add(4).add(5).add(1).add(9).add(6).add(4).add(4).add(1).add(8).add(4).add(8).add(9).add(3);
    // remove all duplicates from the list
    list.removeDuplicates();
    // show the list
    console.log(list);
}
// run the main function
NodeStuff();

// this is the values of the list before running removeDuplicates()
// [1,2,8,0,9,3,5,9,9,7,4,5,1,9,6,4,4,1,8,4,8,9,3]
// this is the values of the list after running removeDuplicates()
// [2,0,7,6]