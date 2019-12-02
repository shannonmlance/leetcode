var deleteDuplicates = function(head) {
    if (head == null) {
        return head;
    }
    else if (head.next == null) {
        return head;
    } else {
        var current = head;
        var previous = head;
        while (previous.next != null) {
            var foundDup = false;
            var runner = current;
            while (runner.next != null) {
                if (current.val == runner.next.val) {
                    foundDup = true;
                    runner.next = runner.next.next;
                } else {
                    runner = runner.next;
                }
            }
            if (foundDup == true) {
                if (current == head) {
                    head = head.next;
                } else {
                    previous.next = previous.next.next;
                    current = previous.next;
                }
            } else {
                if (current == head) {
                    current = current.next;
                } else {
                    current = current.next;
                    previous = previous.next;
                }
            }
        }
        return head;
    }
};