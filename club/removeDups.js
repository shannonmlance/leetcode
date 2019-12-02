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
};