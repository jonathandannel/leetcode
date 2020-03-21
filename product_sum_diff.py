# Given an integer number n, return the difference between
# the product of its digits and the sum of its digits.
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

def subtractProductAndSum(self, n: int) -> int:
    digits = [int(x) for x in list(str(n))]
    p = digits[0]
    s = digits[0]
    for d in range(1, len(digits)):
        p *= digits[d]
        s += digits[d]
    return p - s