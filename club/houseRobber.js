/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.
*/

// my solution - binary tree
function rob(nums) {
    class BTNode {
        constructor(index, value) {
            this.index = index;
            this.value = value;
            this.skipOne = null;
            this.skipTwo = null;
        }
    };

    class BinaryTree {
        constructor() {
            this.root = null;
        }
        add(index, value) {
            var newNode = new BTNode(index, value);
            if (this.root == null) {
                this.root = newNode;
            }
            else {
                this.addR(this.root, newNode);
            }
            return this;
        }
        addR(node, newNode) {
            if (node.skipOne == null && newNode.index == node.index + 2) {
                node.skipOne = newNode;
            }
            else if (node.skipTwo == null && newNode.index == node.index + 3) {
                node.skipTwo = newNode;
            }
            else if (node.skipOne == null && node.skipTwo == null) {
                return this;
            }
            else {
                this.addR(node.skipOne, newNode);
                newNode = new BTNode(newNode.index, newNode.value);
                this.addR(node.skipTwo, newNode);
            }
            return this;
        }
        sumR(node, num, arr) {
            num += node.value;
            if (node.skipOne != null) {
                this.sumR(node.skipOne, num, arr);
            }
            if (node.skipTwo != null) {
                this.sumR(node.skipTwo, num, arr);
            }
            if (node.skipOne == null && node.skipTwo == null) {
                arr.push(num);
            }
            return arr;
        }
    };

    function robbers(arr) {
        if (arr.length == 0) {
            return 0;
        }
        if (arr.length == 1) {
            return arr[0];
        }
        if (arr.length < 4) {
            var max = arr[0];
            for (var i = 1; i < arr.length; i++) {
                if (arr[i] > max) {
                    max = arr[i];
                }
            }
            return max;
        }
        if (arr.length == 4) {
            var one = arr[0] + arr[2];
            var two = arr[1] + arr[3];
            if (one > two) {
                return one;
            }
            else {
                return two;
            }
        }
        var bt0 = new BinaryTree();
        for (var i = 0; i < arr.length - 1; i++) {
            bt0.add(i, arr[i]);
        }
        var bt1 = new BinaryTree();
        for (var i = 1; i < arr.length; i++) {
            bt1.add(i, arr[i]);
        }
        var bt2 = new BinaryTree();
        for (var i = 2; i < arr.length; i++) {
            bt2.add(i, arr[i]);
        }
        var sum = 0;
        var sumArr = [];
        bt0.sumR(bt0.root, sum, sumArr);
        bt1.sumR(bt1.root, sum, sumArr);
        bt2.sumR(bt2.root, sum, sumArr);
        var max = sumArr[0];
        for (var i = 1; i < sumArr.length; i++) {
            if (sumArr[i] > max) {
                max = sumArr[i];
            }
        }
        return max;

    }
    robbers(nums);
};

// my solution - comparison

// for leetcode
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {

};