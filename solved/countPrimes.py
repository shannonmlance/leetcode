# Count the number of prime numbers less than a non-negative number, n.

# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10. They are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n):
        # there are no prime numbers less than 2
        if n <= 2: return 0
        # create an array for marking primes less than the given number
        # by default, every number is a prime
        # 1 == True
        isPrime = [1] * n
        # zero and one are not primes
        # 0 == False
        isPrime[0] = isPrime[1] = 0
        # iterator for moving through array
        i = 2
        # only need to check a number if its square is less than the given number
        while i*i < n:
            # only need to check a number if it is True
            if isPrime[i] == 1:
                # by default, all multiples of a number cannot be prime, so for our current number, change all multiples to False
                isPrime[i*i: n: i] = [0] * (1 + (n - i*i - 1) // i)
                    # breakdown of the above line:
                        # isPrime[i*i: n: i] means
                            # for j in range(i*i, n, i):
                            # which means loop through starting at i*i, going until n (exclusive), and incrementing by i
                        # [0] * (1 + (n - i*i - 1) // i) means
                            # [0] is the fill amount: isPrime[j] = [0]
                            # 1 + (n - i*i - 1) // i is equal to the number of multiples of i from i*i to n
                    # example:
                        # i == 5, n == 100
                        # isPrime[5*5: 100: 5] = [0] * (1 + (100 - 5*5 - 1) // 5)
                        # for j in range(25, 100, 5):
                            # isPrime[j] = 0
                            # (this will happen 15 times)
            # this ensures we don't check all even numbers, only the first (2)
            # can also be written:
                # if i == 2:
                    # i += 1
                # else:
                    # i += 2
            i += 1 if i == 2 else 2
        # since prime numbers are marked with a 1 value, we can just sum up the values in the array
        return sum(isPrime)

class goodSolution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        i = 2
        while i*i < n:
            j = i*i
            while j < n:
                isPrime[j] = False
                j += i
            i += 1
        count = 0
        i = 2
        while i < n:
            if isPrime[i] == True:
                count += 1
            i += 1
        return count

class myOptimalSolution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count
    def isPrime(self, n):
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

import math

class mySolution:
    def countPrimes(self, n):
        # quick exit
        # if the given number is less than 2, there can be no primes
        if n < 3:
            return 0
        # initiate variable for counting primes
        count = 0
        # loop through the given number, exclusive of 1 and the given number
        for i in range(2, n):
            # set variable for saving response from helper function
            b = self.isPrime(i)
            # if helper function returned true, increment prime counter
            if b == True:
                count += 1
        return count
    # helper function for determining if a number is a prime
    def isPrime(self, n):
        # loop through the given number, exclusive of 1 and the given number
        for i in range(2, n):
            # divide the given number by the loop number
            d = n / i
            # determine the remainder when the answer from the division problem above is divided by the whole number answer from the division problem above
            p = d % math.floor(d)
            # if the remainder is zero, then the loop number is a factor of the given number and therefore the given number cannot be prime
            if p == 0:
                return False
        # if no factors have been located, then the given number is prime
        return True

n = 120
s = Solution()
a = s.countPrimes(n)
print("@"*20)
print(a)
