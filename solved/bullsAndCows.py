# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. Please note that both secret number and friend's guess may contain duplicate digits.

# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

# Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

from collections import Counter

class Solution:
    def getHint(self, secret, guess):
        # initiate bulls and cows counters
        bulls = cows = 0
        # zip the secret and guess and return a list
        l = list(zip(secret, guess))
        # initiate an iterator
        i = 0
        # loop through the list
        while i < len(l):
            # if the both items in the tuple from zipping are the same
            if l[i][0] == l[i][1]:
                # increment the bulls counter
                bulls += 1
                # remove the tuple from the list
                l.remove(l[i])
            # if both items in the tuple from zipping are not the same
            else:
                # increment the iterator
                i += 1
        # initiate a dictionary with counter()
        d = Counter()
        # loop through the list
        for i in l:
            # add the first item in each tuple to the dictionary as the key, and count how many of each key there is
            d[i[0]] += 1
        # same as above, but written without counter()
        # d = {}
        # for i in l:
        #     if i[0] in d:
        #         d[i[0]] += 1
        #     else:
        #         d[i[0]] = 1
        # initiate an incrementor
        i = 0
        # loop through the list
        while i < len(l):
            # if the second item in the tuple is in the dictionary
            if l[i][1] in d:
                # if the count for the second item in the tuple is 1
                if d[l[i][1]] == 1:
                    # remove that item from the dictionary
                    d.pop(l[i][1])
                # if the count for the second item in the tuple is not 1
                else:
                    # decrement the count for that item
                    d[l[i][1]] -= 1
                # increment the cows count
                cows += 1
            # increment the iterator
            i += 1
        # build the answer string
        hint = str(bulls) + "A" + str(cows) + "B"
        return hint

secret = "1900"
guess =  "0090"
s = Solution()
a = s.getHint(secret, guess)
print(a)
