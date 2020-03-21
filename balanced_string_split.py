# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into 
# "RL", "RRLL", "RL", "RL", 
# each substring contains same number of 'L' and 'R'.

def balancedStringSplit(s: str) -> int:
    if len(s) < 1 or len(s) > 1000:
        return 0  
    count = 0
    r = 0
    l = 0
    for letter in list(s):
        if letter is "R":
            r += 1
        if letter is "L":
            l += 1
        if r == l:
            count += 1
    return count