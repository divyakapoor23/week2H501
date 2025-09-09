import numpy as np


"""
    Given a number n, return the number of ways to make change 
    for n cents using only 5 cent coins
"""
def ways(cents, coin_types=[1, 5]):
    # Dynamic programming approach for arbitrary coin types
    dp = [0] * (cents + 1)
    dp[0] = 1
    # Iterate over each coin type
    for coin in coin_types:
        # Update the dp array for each amount from coin to cents
        for i in range(coin, cents + 1):
            # Update the number of ways to make change for amount i
            dp[i] += dp[i - coin]
    # Return the number of ways to make change for cents
    return dp[cents]

            # def ways(n):
            #     if n < 0:
            #         return 0;
            #     return n // 5 + 1


""" 
    Given a list of names and a list of scores, 
    return the name with the lowest score
"""
def lowest_score(names, scores):
    # if len(names) != len(scores):
    names = np.array(names)
    scores = np.array(scores)
    # Find the index of the minimum score
    idx = np.argmin(scores)
    # Return the name corresponding to the minimum score
    return names[idx]

"""
    Given a list of names and a list of scores, 
    return the names sorted by their scores in descending order
"""
def sort_names(names, scores):
    # if len(names) != len(scores):
    names = np.array(names)
    scores = np.array(scores)
    # if len(names) != len(scores):
    idx_sorted = np.argsort(scores)[::-1]
    # Return the names sorted by scores in descending order
    return names[idx_sorted]
    
# Test cases

print(ways(12))
print(ways(20))
print(ways(3))
print(ways(0))
print(lowest_score(['A', 'B', 'C'], [90, 80, 85]))
print(sort_names(['A', 'B', 'C'], [90, 80, 85]))