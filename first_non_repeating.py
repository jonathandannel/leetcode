def first_non_repeating(s: str) -> str:
    # char, index
    hash = {}
    for i in range(len(s)):
        current = s[i]
        if not current in hash:
            hash[current] = i
        elif current in hash:
            hash.pop(current)
        if i == len(s) - 1:
            return list(hash.keys()).pop()