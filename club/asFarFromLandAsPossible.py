# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
# If no land or water exists in the grid, return -1.

# Example 1:
# Input: [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.

# Example 2:
# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.
 
# Note:
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] is 0 or 1

from random import randint
from collections import deque

class Solution:
    def maxDistance(self, grid):
        print("Finding the max distance")
        # store the length of the grid in a variable for easy reference
        l = len(grid)
        # create a queue of all the "1s" in the grid, using their x,y coordinates
        q = deque([])
        for i in range(l):
            for j in range(l):
                if grid[i][j] == 1:
                    q.append((i,j))
        # all of the above in one line - cool!
        # q = deque([(i,j) for i in range(l) for j in range(l) if grid[i][j]==1])
        # check for grid containing only "1s" or "0s"
        if len(q) == l*l or len(q) == 0:
            print("Grid contains only 1s or 0s, not both")
            return -1
        # count for distance from 1s
        dist = 0
        while len(q) > 0:
            print("length of queue:", len(q))
            # for each point in the queue
            for v in range(len(q)):
                # take one current point
                i,j = q.popleft()
                # for each direction
                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # create the coordinates for each direction from the current point
                    xi,yj = x+i, y+j
                    # if the new coordinates are within the grid parameters, and have a value of "0"
                    if 0 <= xi < l and 0 <= yj < l and grid[xi][yj] == 0:
                        # add that point to the queue, because we can keep expanding from there
                        q.append((xi,yj))
                        # turn "0" into something else to avoid looping
                        grid[xi][yj] = dist + 2
                        print("Updated grid:\n", grid)
            # increase distance from original "1s"
            dist += 1
            print("Current distance:", dist)
        # return one less than the final number, because the last pass through contains no 0s
        return dist - 1
    def makeGrid(self):
        n = randint(1,10)
        print("grid will be", n, "x", n)
        g = []
        for i in range(n):
            g.append([])
            for j in range(n):
                o = randint(0,1)
                g[i].append(o)
        print(g)
        return g

s = Solution()
grid = s.makeGrid()
a = s.maxDistance(grid)
print(a)
