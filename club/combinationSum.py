# Given a set of candidate numbers, without duplicates, and a target number, find all unique combinations in candidates where the candidate numbers sums to target. The same repeated number may be chosen from candidates unlimited number of times.

# Note:
# All numbers, including target, will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output:
#   [
#       [7],
#       [2,2,3]
#   ]

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output:
#   [
#       [2,2,2,2],
#       [2,3,3],
#       [3,5]
#   ]

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        sums = []
        return sums

class badSolution:
    def combinationSum(self, candidates, target):
        print("running main method")
        candidates.sort()
        print("sorted candidates:", candidates)
        sums = []
        print("empty array to store solution:", sums)

        print("calling recursive method from main method")
        s = self.comboSum(candidates, target, [])
        print("received a solution from recursive method:", s)
        sums.append(s)
        print("added solution to solution array:", sums)
        return sums

    def comboSum(self, candidates, target, selected):
        print("*"*80)
        print("running recursive method")
        print("received the following parameters:", candidates, target, selected)

        if target == 0:
            print("target equals", target)
            print("returning selected candidates:", selected)
            return selected

        for c in candidates:
            print("looking at one candidate:", c)

            if c > target:
                print(c, "is greater than", target)
                break

            if selected != [] and c < selected[len(selected)-1]:
                print("selected holds values:", selected)
                print(c, "is less than", selected[len(selected)-1])
            
            else:
                print("running recursive method from inside recursive method")
                selected.append(c)
                print("passing in the following parameters:", candidates, target-c, selected)
                self.comboSum(candidates, target-c, selected)
        return

candidates = [2,3,6,7]
target = 7
s = Solution()
a = s.combinationSum(candidates, target)
print(a)