#!/bin/bash

# Given a text file file.txt, print just the 10th line of the file.

# Example:
# Assume that file.txt has the following content:
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10

# Your script should output the tenth line, which is:
# Line 10

# Note:
# If the file contains less than 10 lines, what should you output?
# There's at least three different solutions. Try to explore all possibilities.

tail -n +10 supportingDocs/tenthLine.txt | head -n 1